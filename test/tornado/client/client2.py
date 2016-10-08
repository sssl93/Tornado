# coding:utf-8
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

from tornado import gen


@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    # 在Python 3.3之前, 在generator中是不允许有返回值的
    # 必须通过抛出异常来代替.
    raise gen.Return(response.body)


if __name__ == '__main__':
    url = 'http://localhost:8080'
    x = fetch_coroutine(url)
    print x
