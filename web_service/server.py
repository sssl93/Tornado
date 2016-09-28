import tornado.options
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.httpclient
import json

from tornado.options import define, options

define("port", default=8001, help="run on the given port", type=int)


class ServerSync(tornado.web.RequestHandler):
    # def __init__(self, key):
    #     self.key = key

    @tornado.web.asynchronous
    def get(self, key):
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://localhost:10000/?key=%s" % key, callback=self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)
        print body
        self.finish()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/(.*)", ServerSync)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
