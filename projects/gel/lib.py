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
    proc = subprocess.Popen(['convert','-quality','100',oldname,newname])
    proc.wait()
    print "converting", oldname, "to", newname
    return {"download":newname}
    
def KMeans(self):
    files = self.request.files["file[]"]
    jpgfiles = []
    
    #TODO: Find Cy3 and Cy5 based on names! 
    # I am assuming Cy3 is first and Cy5 is second and there are only 2.
    for f in files:
        jpgf = convertFile(f)
        jpgfiles.append(jpgf["download"])
    cy3file = jpgfiles[0]
    cy5file = jpgfiles[1]
    
    k = int(self.get_argument('K',''))
    bands = int(self.get_argument('Bands',''))
    outfile = cy3file+"_kmeans_%d.png"%k
    inputs = {'k':k, 
    'num_bands':bands,
    'cy3_file':cy3file,
    'cy5_file':cy5file,
    'outfile':outfile}
    output = run_kmeans_clustering(**inputs)
    return {"download":output}