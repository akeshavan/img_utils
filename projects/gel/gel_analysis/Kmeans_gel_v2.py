# -*- coding: utf-8 -*-
#from nipype import config
#config.enable_debug_mode()
import matplotlib
matplotlib.use("agg")
from matplotlib.pyplot import imread, savefig,subplots,cm
import numpy as np
import uuid
import os
from utils import split_filename

def invert(img):
    from copy import deepcopy
    imin = np.min(img)
    imax = np.max(img)
    img_inv = imax - deepcopy(img)+imin
    return img_inv


# KMeans



def kmeans(img,nlabels=5):
    import os
    from matplotlib.pyplot import imread, imsave
    from sklearn import cluster
    from nipype.utils.filemanip import split_filename
    import numpy as np
    import scipy.io as sio
    lena = imread(img)
    X = lena.reshape((-1, 1)) # We need an (n_sample, n_feature) array
    k_means = cluster.KMeans(n_clusters=nlabels, n_init=1)
    k_means.fit(X) 
    values = k_means.cluster_centers_.squeeze()
    labels = k_means.labels_
    outkmeans = labels.reshape(lena.shape)
    loc, name, ext = split_filename(img)
    outfile = os.path.abspath(name+"_kmeans.mat")
    sio.savemat(outfile,{"kmeans":outkmeans})
    print outfile, "exists", os.path.exists(outfile)
    return outfile


def split_k(in_file):
    import numpy as np
    from matplotlib.pyplot import imread, imsave
    from nipype.utils.filemanip import split_filename
    import os
    import scipy.io as sio
    data = np.asarray(sio.loadmat(in_file)["kmeans"])
    vals = np.unique(data)
    _, name, ext = split_filename(in_file)
    outfiles = []
    for v in vals:
        outfile = os.path.abspath(name+"_k%02d"%(v)+".mat")
        print outfile
        sio.savemat(outfile,{"k":data==v})
        outfiles.append(outfile)
    return outfiles
    
# Labeling and Centroid Calculation


def get_labels(data_file, min_extent=100):
    from nipype.utils.filemanip import split_filename
    from scipy.ndimage import label
    import os
    import scipy.io as sio
    import numpy as np
    data = sio.loadmat(data_file)
    labels, nlabels = label(data["k"] == 0)
    for idx in range(1, nlabels+1):
        if np.sum(labels==idx)<min_extent:
            labels[labels==idx] = 0
    nlabels = len(np.unique(labels))
    _,name,ext = split_filename(data_file)
    outfile = os.path.abspath(name+"_label.mat")
    sio.savemat(outfile,{"label":labels})
    return outfile, nlabels



def get_centroids(labels):
    labelnums = np.unique(labels)
    centroids = []
    for label in labelnums:
        centroids.append(np.mean(np.asarray(np.nonzero(labels==label)), axis = 1))
    return centroids



def choose_k(labelfiles,cy3file):
    from nipype.utils.filemanip import split_filename
    from matplotlib.pyplot import imread
    import numpy as np
    import scipy.io as sio
    cy3 = imread(cy3file)
    means = []
    nums = []
    for l in labelfiles:
        print l
        label = sio.loadmat(l)["k"]
        label = np.asarray(label).astype(bool)
        mean = np.mean(cy3[label])
        means.append(mean)
        num = np.sum(label)
        nums.append(num)
    #idx = means.index(np.min(np.asarray(means)[np.asarray(num)>=numbands]))
    idx = np.argmax(means) #I think 255 is the blackest value
    return idx,labelfiles[idx]
    
# Plotting



def plot_histograms(cy3,cy5):
    fig,ax = subplots(ncols=2,nrows=1,figsize=(12,6))
    ax[0].hist(cy3.ravel(),bins=100,color="black");
    ax[0].set_title("Cy3 Histogram")
    ax[1].hist(cy5.ravel(),bins=100,color="black");
    ax[1].set_title("Cy5 Histogram")



def make_boxplot(measure_names,cy5,cy3,title=''):
    import scipy.stats as stats
    ind = np.arange(len(measure_names))
    width = 0.35

    fig = plt.figure(figsize=(24,8))
    ax = fig.add_subplot(111)
    
    rects1 = ax.boxplot(cy3,positions = ind,widths=0.2)
    rects2 = ax.boxplot(cy5,positions = [i+width for i in ind],widths=0.2)
    ax.set_xticklabels(measure_names,rotation=0)
    p1 = [plot(np.ones(len(cy3[i]))*ind[i],cy3[i],'ro',alpha=0.005) for i in range(len(measure_names))]
    c1 = [plot(np.ones(len(cy5[i]))*ind[i]+width,cy5[i],'bo',alpha=0.005) for i in range(len(measure_names))]
    
    for key in rects1.keys():
        setp(rects1[key],color='red')
        setp(rects2[key],color='blue')
    
    ax.set_ylabel('Intensity')
    ax.set_xlabel('MgCl2 concentration')
    ax.set_title(title)
    ax.set_xticks(ind+width/2)
    ax.legend( (rects1[key][0], rects2[key][0]), ('Cy3', 'Cy5') )



def plotallimages(cy3file,cy5file,labelsfile,Clustersfile):
    from matplotlib.pyplot import imread, savefig,subplots,cm
    from nipype.utils.filemanip import split_filename
    import os
    import numpy as np
    import scipy.io as sio
    
    def get_centroids(labels):
        labelnums = np.unique(labels)
        centroids = []
        for label in labelnums:
            centroids.append(np.mean(np.asarray(np.nonzero(labels==label)), axis = 1))
        return centroids
    
    cy3 = imread(cy3file)
    cy5=imread(cy5file)
    Clusters = np.asarray(sio.loadmat(labelsfile)["label"])
    labels = np.asarray(sio.loadmat(Clustersfile)["k"])
    _,name,ext = split_filename(Clustersfile)
    outfile = os.path.abspath(name+"_img_all.png")
    
    fig,ax = subplots(ncols=4,nrows=1,figsize=(36,12))
    ax[0].imshow(cy3,cmap=cm.Greys)
    k = len(np.unique(labels))
    cmap = cm.get_cmap('jet', k)
    l = ax[1].imshow(labels,cmap=cmap)
    ax[1].set_title('K Means Clustering')
    
    nlabels = len(np.unique(Clusters))
    cmap = cm.get_cmap('jet', nlabels)
    b=ax[2].imshow(Clusters,cmap=cmap,alpha=0.3)
    ax[2].set_title("ROI Labelling")
    centroids = get_centroids(Clusters)
    for i,c in enumerate(centroids):
        ax[2].annotate('%d'%i,c[::-1],color="black");
    ax[3].imshow(cy5,cmap=cm.Greys)
    ax[3].set_title('Cy5 - Defect')
    ax[0].set_title('Cy3 - Object')
    savefig(outfile,bbox_inches="tight")
    return outfile


# Function that combines all



def run_kmeans_clustering(k,num_bands,cy3_file,cy5_file,outfile):
    cy3 = imread(cy3_file)
    cy5 = imread(cy5_file)
    labels = kmeans(cy3,k)
    Kidx, Clusters = choose_k(labels,cy3,num_bands)
    outfile = plotallimages(cy3,cy5,labels,Clusters,outfile)
    return outfile
    

def create_workflow(cy3_file, cy5_file,k, min_extent=100):
    import nipype.pipeline.engine as pe
    import nipype.interfaces.utility as util
    from nipype.utils.filemanip import split_filename
    import nipype.interfaces.io as nio

    wfuuid = uuid.uuid1().hex
    wf = pe.Workflow(name="Kmeans_segmentation_%s"%wfuuid)
    km = pe.Node(util.Function(input_names=["img","nlabels"],
                               output_names=["outfile"],
                               function=kmeans),
                 name="Kmeans")
    km.inputs.img = cy3_file
    km.inputs.nlabels = k
    
    splitk = pe.Node(util.Function(input_names=["in_file"],
                                   output_names=["outfiles"],
                                   function=split_k),
                     name="split_k")
                     

    getlabels = pe.Node(util.Function(input_names=["data_file","min_extent"],
                                         output_names=["outfile","n_labels"],
                                         function=get_labels),
                           name="get_labels")

    getlabels.inputs.min_extent = min_extent
    
    choosek = pe.Node(util.Function(input_names=["labelfiles","cy3file"],
                                    output_names=["idx","labelfile"],
                                    function=choose_k),name="choose_k")

    choosek.inputs.cy3file = cy3_file

    plotter = pe.Node(util.Function(input_names=["cy3file","cy5file","labelsfile","Clustersfile"],
                                    output_names=["outfile"],
                                    function=plotallimages),
                      name="plot_images")

    plotter.inputs.cy3file = cy3_file
    plotter.inputs.cy5file = cy5_file
    
    subs = [("_get_labels%d"%i, "") for i in range(5)]
    
    sinker = pe.Node(nio.DataSink(),name="sinker")
    sinker.inputs.base_directory = os.path.abspath("downloads")
    sinker.inputs.container = "%s"%(wfuuid)
    sinker.inputs.substitutions = subs

    wf.connect(km,"outfile",splitk,"in_file")
    wf.connect(getlabels,"outfile",plotter,"labelsfile")
    wf.connect(splitk,"outfiles",choosek,"labelfiles")
    wf.connect(choosek,"labelfile", getlabels,"data_file")

    wf.connect(choosek,"labelfile",plotter,"Clustersfile")

    wf.connect(km,"outfile",sinker,"kmeans")
    wf.connect(getlabels,"outfile",sinker,"labelfiles")
    wf.connect(plotter,"outfile",sinker,"image")



    wf.base_dir = "/Users/keshavan/Projects/img_utils/working_dir"
    wf.config["execution"] = {"remove_unnecessary_outputs":False}
    wf.write_graph()
    wf.run()
# 42X Noodle
    return os.path.join("downloads/%s"%wfuuid)

# Define Parameters:


if __name__ == "__main__":

    p42X = {'k':5, 
            'cy3_file':'../../../downloads/10282013_42XCy3_D_O_3H_70V-[Cy3].jpg',
            'cy5_file':'../../../downloads/10282013_42XCy3_D_O_3H_70V-[Cy5].jpg'}


    create_workflow(**p42X)
    #run_kmeans_clustering(**p42X)


    # 84X Noodle



    p84X = {'k':3, 
            'cy3_file':'../downloads/10232013_84XCy3_D_O_3H_70V-[Cy3].jpg',
            'cy5_file':'../downloads/10232013_84XCy3_D_O_3H_70V-[Cy5].jpg'}







