# coding:utf-8
from tweet_rate import IndexHandler
import threading, json
import tornado
import time


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
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("http://localhost:10000/?key=%s" % self.key, callback=self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)
        print body


if __name__ == '__main__':
    now = time.time()
    for key in range(20):
        t = MyThread(key)
        t.start()
