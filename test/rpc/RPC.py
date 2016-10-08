import functools
import xmlrpclib

HOST = 'localhost'
PORT = 48068
DB = 'damo'
USER = 'system'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)


def xmlrpc():
    # 1. Login
    uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
    print "Logged in as %s (uid:%d)" % (USER, uid)

    call = functools.partial(
        xmlrpclib.ServerProxy(ROOT + 'object').execute,
        DB, uid, PASS)

    # 2. Read the sessions
    #  'openacademy.session'  is a table in the DB
    sessions = call('openacademy.session', 'search_read', [], ['name', 'seats'])
    for session in sessions:
        print "Session %s (%s seats)" % (session['name'], session['seats'])
    # 3.create a new session
    session_id = call('openacademy.session', 'create', {
        'name': 'My session',
        'course_id': 2,
    })



