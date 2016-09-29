# coding=utf-8
import requests

baseurl = 'http://192.168.1.200:15673'
auth = ('guest', 'guest')

# 删除exchange
result = requests.get(baseurl + '/api/exchanges/%2f', auth=auth).json()
for exchange in result:
    name = exchange['name']
    if name:
        if not name.startswith('amq.'):
            requests.delete(baseurl + '/api/exchanges/%2f/' + name, auth=auth)

# 删除queue
result = requests.get(baseurl + '/api/queues/%2f', auth=auth).json()
for queue in result:
    name = queue['name']
    requests.delete(baseurl + '/api/queues/%2f/' + name, auth=auth)
