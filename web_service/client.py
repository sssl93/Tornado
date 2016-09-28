# coding:utf-8
import threading, json
import tornado
import time
import tornado.web
import tornado.httpclient
from server import ServerSync


class MyThread(threading.Thread):
    def __init__(self, key):
        threading.Thread.__init__(self);
        self.key = key

    # def run(self):
    #     # 同步调用
    #     client = tornado.httpclient.HTTPClient()
    #     response = client.fetch("http://localhost:10000/?key=%s" % self.key)
    #     body = json.loads(response.body)
    #     print body

    def run(self):
        # 异步调用
        # client = tornado.httpclient.AsyncHTTPClient()
        # response = client.fetch("http://localhost:10000/?key=%s" % self.key, callback=self.on_response)
        import requests
        requests.get('http://localhost:8001/%s' % self.key)

    def on_response(self, response):
        body = json.loads(response.body)
        print body


if __name__ == '__main__':
    now = time.time()
    for key in range(20):
        t = MyThread(key)
        t.start()
