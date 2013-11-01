from gel_analysis.Kmeans_gel_v2 import run_kmeans_clustering
from nipype.utils.filemanip import split_filename
import subprocess
import os

    
def getname(filename):
    _,name,ext = split_filename(filename)
    oldname = os.path.join('uploads',name+ext)
    newname = os.path.join('downloads',name+'.jpg')
    return oldname, newname
    
    
def convertFile(files):
    oldname, newname = getname(files["filename"])
    foo = open(oldname,'w')
    foo.write(files["body"])
    foo.close()
    proc = subprocess.Popen(['sleep','10'])#'convert','-quality','100',oldname,newname])
    proc.wait()
    print "converting", oldname, "to", newname
    return newname
    
def KMeans(self):
    files = self.request.files["file[]"]
    jpgfiles = []
    for f in files:
        jpgf = convertFile(f)
        jpgfiles.append(jpgf)
    cy3file = jpgfiles[0]
    cy5file = jpgfiles[1]
    k = int(self.get_argument('K',''))
    bands = int(self.get_argument('Bands',''))
    inputs = {'k':k, 
    'num_bands':bands,
    'cy3_file':cy3file,
    'cy5_file':cy5file}
    run_kmeans_clustering(**inputs)