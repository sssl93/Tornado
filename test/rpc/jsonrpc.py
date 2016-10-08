import json
import random
import urllib2

HOST = 'localhost'
PORT = 48068
DB = 'damo'
USER = 'system'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# The following example is a Python program that interacts with an Odoo server with the standard Python libraries urllib2 and json
def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib2.Request(url=url, data=json.dumps(data), headers={
        "Content-Type": "application/json",
    })
    reply = json.load(urllib2.urlopen(req))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

# log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

# create a new note
args = {
    'color': 8,
    'memo': 'This is another note',
    'create_uid': uid,
}
# 'note.note'  is a table
note_id = call(url, "object", "execute", DB, uid, PASS, 'note.note', 'create', args)