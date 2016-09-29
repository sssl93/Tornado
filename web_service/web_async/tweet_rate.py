# coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib
import json
import datetime
import time

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, key):
        # 显示从获取请求到response所花费的时间
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("http://localhost:10000/?key=%s" % key)
        body = json.loads(response.body)
        raw_oldest_tweet_at = body[1]
        now = datetime.datetime.now()
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                                                     "%Y-%m-%d %H:%M:%S")
        seconds_diff = time.mktime(now.timetuple()) - time.mktime(oldest_tweet_at.timetuple())
        print str(key) + ':>>>' + str(seconds_diff)
        self.write("""
<div style="text-align: center">
    <div style="font-size: 72px">%s</div>
    <div style="font-size: 144px">%.02f</div>
    <div style="font-size: 24px">tweets per second</div>
</div>""" % (body[0], seconds_diff))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/(.*)", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
