import json
import random
import urllib2

HOST = 'localhost'
PORT = 48068
DB = 'damo'
USER = 'system'
PASS = 'admin'
url = 'http://%s:%d/jsonrpc/' % (HOST, PORT)


def json_rpc(url, method, params):
    data = {
        'params': {
            'args': [
                'damo',  # DB name
                1,  # DB user id
                'admin',  # DB password
                'res.users',  # table(class)
                'search_read',  # method of class
                [('id', '=', 1)],
            ],
            'method': 'execute',
            'service': 'object'
        },
        'jsonrpc': '2.0',
        'method': 'call',
        'id': 241176636
    }
    req = urllib2.Request(url=url, data=json.dumps(data), headers={
        "Content-Type": "application/json",
    })
    reply = json.load(urllib2.urlopen(req))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]


if __name__ == '__main__':
    json_rpc(url, 1, 1)
