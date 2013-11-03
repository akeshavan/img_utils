"""
Handlers
"""

import tornado.web
from tornado.web import asynchronous
from tornado.escape import json_encode
import tornadio2.router
import tornadio2
import tornadio2.server
#import lib
import json
from tornado.escape import json_encode
#import tornadio2.web



# files to store handlers
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    moduleName=""
                   )

from projects.tif.handlers import FileUploadHandler
from projects.gel.handlers import FileGelUploadHandler






       

