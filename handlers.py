"""
Handlers
"""

import tornado.web
from tornado.web import asynchronous
from tornado.escape import json_encode
import tornadio2.router
import tornadio2
import tornadio2.server
import lib
#import tornadio2.web




# files to store handlers
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    moduleName=""
                   )


class FileUploadHandler(tornado.web.RequestHandler):
    def get(self):
        pass
        return
        
    @asynchronous
    def post(self):
        files = self.request.files["file"][0]
        lib.convertFile(files)
        self.render("index.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    moduleName="",
                   )


class FileGelUploadHandler(tornado.web.RequestHandler):
    def get(self):
        pass
        return
        
    @asynchronous
    def post(self,*args,**kwargs):

        lib.KMeans(self)

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
        _,newname = lib.getname(message)
        self.send(newname)
        
        
    def close(self):
        self.connections.remove(self)
        print "connection closed"

DLRouter = tornadio2.router.TornadioRouter(FileDownloadReady, {'enabled_protocols': ['websocket','flashsocket','xhr-multipart','xhr-polling']})

