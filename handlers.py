"""
Handlers
"""

import tornado.web
from tornado.escape import json_encode
from nipype.utils.filemanip import split_filename
import subprocess
import os
import tornadio2.router
import tornadio2
import tornadio2.server
#import tornadio2.web

# files to store handlers
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    moduleName=""
                   )

def getname(filename):
    _,name,ext = split_filename(filename)
    oldname = os.path.join('uploads',name+ext)
    newname = os.path.join('downloads',name+'.png')
    return oldname, newname


def convertFile(files):
    oldname, newname = getname(files["filename"])
    foo = open(oldname,'w')
    foo.write(files["body"])
    foo.close()
    proc = subprocess.Popen(['convert','-quality','100',oldname,newname])
    proc.wait()
    print "converting", oldname, "to", newname
    return newname

class FileUploadHandler(tornado.web.RequestHandler):
    def get(self):
        pass
        return

    def post(self):
        files = self.request.files["file"][0]
        convertFile(files)
        self.render("index.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    moduleName="",
                   )


class SocketIOHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('static/js/socket.io.js')

class FileDownloadReady(tornadio2.conn.SocketConnection):
    connections = []

    def open(self):
        self.connections.append(self)

    def on_message(self,message):
        # TODO: Check that the proc is complete!! When it is complete, send the message
        print message
        #newfile = convertFile(message)
        _,newname = getname(message)
        self.send(newname)
        
        
    def close(self):
        self.connections.remove(self)
        print "connection closed"

DLRouter = tornadio2.router.TornadioRouter(FileDownloadReady, {'enabled_protocols': ['websocket','flashsocket','xhr-multipart','xhr-polling']})

