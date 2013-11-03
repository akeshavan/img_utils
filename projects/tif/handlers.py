import tornado.web
from tornado.web import asynchronous
from tornado.escape import json_encode
import tornadio2.router
import tornadio2
import tornadio2.server
import lib as tiflib
import json
from tornado.escape import json_encode

class FileUploadHandler(tornado.web.RequestHandler):
    def get(self):
        pass
        return
        
    @asynchronous
    def post(self):
        files = self.request.files["file"][0]
        info = tiflib.convertFile(files)
        
        self.write(json_encode(info))
        self.finish()