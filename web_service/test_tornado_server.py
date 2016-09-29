# coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import json
import datetime
import time

from tornado.options import define, options

define("port", default=10000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        key = self.get_argument('key', )
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = key + ':>>>' + now
        time.sleep(0.5)
        print data
        data = json.dumps((data, now))
        self.write(data)


if __name__ == "__main__":
    # tornado同步server
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
