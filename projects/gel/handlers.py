import tornado.web
from tornado.web import asynchronous
from tornado.escape import json_encode
import tornadio2.router
import tornadio2
import tornadio2.server
import lib as gellib
import json
from tornado.escape import json_encode

class FileGelUploadHandler(tornado.web.RequestHandler):
    def get(self):
        pass
        return
        
    @asynchronous
    def post(self,*args,**kwargs):

        info = gellib.KMeans(self)
        self.write(json_encode(info))
        self.finish()