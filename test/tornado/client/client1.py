# coding:utf-8
from tornado.httpclient import HTTPClient


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body

if __name__ == '__main__':
    url = 'http://localhost:8080'
    print synchronous_fetch(url)