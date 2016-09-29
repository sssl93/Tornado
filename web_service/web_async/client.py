# coding:utf-8
import threading, json
import tornado
import time
import tornado.web
import tornado.httpclient


class MyThread(threading.Thread):
    def __init__(self, key):
        threading.Thread.__init__(self)
        self.key = key

    def run(self):
        # 多线程发送请求，模拟异步发送请求
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("http://localhost:8001/%s" % self.key)
        body = response.body
        print body


if __name__ == '__main__':
    now = time.time()
    for key in range(20):
        t = MyThread(key)
        t.start()
