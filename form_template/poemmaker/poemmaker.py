# coding:utf-8
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        '''
        模板语法
        Usage::
        >>> from tornado.template import Template
        >>> content = Template("<html><body><h1>{{ header }}</h1></body></html>")
        >>> print content.generate(header="Welcome!")
        <html><body><h1>Welcome!</h1></body></html>
        填充语法
        Usage::
        >>> from tornado.template import Template
        >>> print Template("{{ 1+1 }}").generate()
        2
        >>> print Template("{{ 'scrambled eggs'[-4:] }}").generate()
        eggs
        >>> print Template("{{ ', '.join([str(x*x) for x in range(10)]) }}").generate()
        0, 1, 4, 9, 16, 25, 36, 49, 64, 81
        '''

        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                    difference=noun3)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/poem', PoemPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

