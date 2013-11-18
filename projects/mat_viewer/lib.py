from nipype.utils.filemanip import split_filename
import subprocess
import os
import scipy.io as sio
from matplotlib.pyplot import imsave, savefig, imshow, annotate, imread, figure
import numpy as np
    
def getname(filename):
    _,name,ext = split_filename(filename)
    oldname = os.path.join('uploads',name+ext)
    newname = os.path.join('downloads',name+'.jpg')
    return oldname, newname
    
    
def get_centroids(labels):
    labelnums = np.unique(labels)
    centroids = []
    for label in labelnums:
        centroids.append(np.mean(np.asarray(np.nonzero(labels==label)), axis = 1))
    return centroids
    
def get_vals(labels,data):
    labelnums = np.unique(labels)
    vals = {}
    vals["roi"] = []
    vals["mean"] = []
    for i,label in enumerate(labelnums):
        vals["mean"].append(np.mean(data[labels==label]))
        vals["roi"].append(i)
    return vals
    
def convert(files):
    oldname, newname = getname(files["filename"])
    foo = open(oldname,'w')
    foo.write(files["body"])
    foo.close()
    
    bar = sio.loadmat(oldname)
    keys = [b for b in bar.keys() if not b.startswith("__")]
    if len(keys)==1:
        data = bar[keys[0]]
        figure(1)
        imshow(data)
        centroids = get_centroids(data)
        for i,c in enumerate(centroids):
            annotate('%d'%i,c[::-1],color="black");
        savefig(newname)
        #imsave(newname,data)
    return {"download":newname}
    
def extract(files):
    
    matfile = [f for f in files if f["filename"].endswith(".mat")][0]
    imgfile = [f for f in files if f["filename"].endswith(".jpg")][0]
    
    oldimgname, newimgname = getname(imgfile["filename"])
    foo = open(oldimgname,'w')
    foo.write(imgfile["body"])
    foo.close()    
    
    oldmatname, newmatname = getname(matfile["filename"])
    foo = open(oldmatname,'w')
    foo.write(matfile["body"])
    foo.close()    
    
    bar = sio.loadmat(oldmatname)
    keys = [b for b in bar.keys() if not b.startswith("__")]
    if len(keys)==1:
        data = bar[keys[0]]
        figure(1)
        imshow(data)
        centroids = get_centroids(data)
        for i,c in enumerate(centroids):
            annotate('%d'%i,c[::-1],color="black");
        savefig(newmatname)
        vals = get_vals(data,imread(oldimgname))
        valsfile = open("downloads/vals.tsv","w")
        valsfile.write("roi\tmean\n")
        for i in range(1,len(vals["roi"])):
            valsfile.write("%d\t%f\n"%(vals["roi"][i],vals["mean"][i]))
        valsfile.close()
    
    #proc = subprocess.Popen(['convert','-quality','100',oldname,newname])
    #proc.wait()
    #print "converting", oldname, "to", newname
    return {"download":newmatname,"vals":"downloads/vals.tsv"}
    
