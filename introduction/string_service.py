# coding:utf-8
import textwrap
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])


class WrapHandler(tornado.web.RequestHandler):
    def head(self, text):
        self.set_status(404)  # 显式设置http状态

    def post(self, text):
        text = text
        # text = self.get_argument('text',default='you are sb zzz!')
        width = self.get_argument('width', default=40)
        self.write(textwrap.fill(text, int(width)))

    def write_error(self, status_code, **kwargs):
        # 重写返回的错误消息
        self.write("Gosh darnit, user! You caused a %d error." % status_code)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/reverse/(\w+)", ReverseHandler),
            (r"/wrap/(\w+)", WrapHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
