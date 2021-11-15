#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import settings

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('{"laws": ["A robot may not injure a human being or, through inaction, allow a human being to come to harm", "A robot must obey the orders given it by human beings except where such orders would conflict with the First Law", "A robot must protect its own existence as long as such protection does not conflict with the First or Second Law"]}')

def make_app(settings={}):
    return tornado.web.Application([(r'/api', MainHandler)], **settings)

if __name__ == '__main__':
    app = make_app(settings.server_settings())
    app.listen(settings.BASE_PORT)  # TODO: increase BASE_PORT by instance index
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt as e:
        pass

    exit(0)
