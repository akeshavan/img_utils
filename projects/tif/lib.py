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