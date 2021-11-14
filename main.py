#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import settings

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('{}')

def make_app(settings={}):
    return tornado.web.Application([(r'/', MainHandler)], **settings)

if __name__ == '__main__':
    app = make_app(settings.server_settings())
    app.listen(settings.BASE_PORT)  # TODO: increase BASE_PORT by instance index
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt as e:
        pass

    exit(0)
