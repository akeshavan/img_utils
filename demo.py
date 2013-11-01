#!/usr/bin/python

from os import path

from tornado import web, ioloop, gen
import os
from handlers import *


def load_app(port, root):
    settings = {
        "static_path": path.join(root, "static"),
        "template_path": path.join(root, "template"),
        "globals": {
            "project_name": "Image Utilities"
        },
        "flash_policy_port": 843,
        "flash_policy_file": path.join(root, 'flashpolicy.xml'),
        "socket_io_port": port,
    }

    routers = [
        (r"/", MainHandler),
        (r'/downloads/(.*)',web.StaticFileHandler,{'path':os.path.join(root,'downloads')}),
        (r"/socket.io.js",SocketIOHandler),
        (r"/file-upload", FileUploadHandler),
        (r"/file-upload-gel", FileGelUploadHandler)
    ]

    try:
        from tornadio2 import TornadioRouter, SocketServer
        from connections import QueryConnection
        # Create tornadio router
        #QueryRouter = TornadioRouter(QueryConnection)
        # Create socket application
        http_application = web.Application(
            #QueryRouter.apply_routes(routers),
            routers,
            **settings
        )
        sock_app = web.Application(DLRouter.urls,socket_io_port=8889)
        #application.listen(8888)
        http_server = tornado.httpserver.HTTPServer(http_application)
        http_application.listen(port)
        SocketServer(sock_app,auto_start=False)
        tornado.ioloop.IOLoop.instance().start()
    except ImportError:
        print "Failed to load module tornadio2"
        application = web.Application(
            routers,
            **settings
        )
        application.listen(port)
        tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":

    root = path.dirname(__file__)
    port = 8888

    load_app(port, root)

