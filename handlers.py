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
import tornado.auth
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

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        return tornado.escape.json_decode(user_json)

class LoginHandler(BaseHandler, tornado.auth.GoogleMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()
 
    def _on_auth(self, user):
        if not user:
            self.send_error(500)
        self.set_secure_cookie("user", tornado.escape.json_encode(user))
        self.redirect("/")



       

