# coding:utf-8
import tornado.options
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.httpclient
import tornado.gen
import json

from tornado.options import define, options

define("port", default=8001, help="run on the given port", type=int)


class ServerSync(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, key):
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://localhost:10000/?key=%s" % key, callback=self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)
        self.write(body)
        print body
        self.finish()


class ServerSync2(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, key):
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch, "http://localhost:10000/?key=%s" % key, )
        body = json.loads(response.body)
        self.write(body[0])
        print body
        self.finish()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    # 这里指定了两种不同的方法实现tornado异步请求

    # app = tornado.web.Application(handlers=[(r"/(.*)", ServerSync)])
    # http_server = tornado.httpserver.HTTPServer(app)

    app2 = tornado.web.Application(handlers=[(r"/(.*)", ServerSync2)])
    http_server = tornado.httpserver.HTTPServer(app2)

    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
