import tornado.web
from tornado.web import asynchronous
from tornado.escape import json_encode
import tornadio2.router
import tornadio2
import tornadio2.server
import lib as matlib
import json
from tornado.escape import json_encode

class MatUploadHandler(tornado.web.RequestHandler):
    def get(self):
        pass
        return
        
    @asynchronous
    def post(self,*args,**kwargs):
        files= self.request.files["file[]"]
        if len(files) == 1:        
            info = matlib.convert(files[0])
            self.write(json_encode(info))
            self.finish()
        elif len(files) == 2:
            info = matlib.extract(files)
            self.write(json_encode(info))
            self.finish()