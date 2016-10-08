import socket
import thread
import urlparse
import select
from db_handler import DBHandler

BUFLEN = 8192


class Proxy(object):
    def __init__(self, conn, addr, lock):
        self.source = conn
        self.request = ""
        self.headers = {}
        self.destnation = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.run()
        lock.release()

    def get_headers(self):
        header = ''
        while True:
            header += self.source.recv(BUFLEN)
            index = header.find('\n')
            if index > 0:
                break
        # firstLine,self.request=header.split('\r\n',1)
        firstLine = header[:index]
        self.request = header[index + 1:]
        self.headers['method'], self.headers['path'], self.headers['protocol'] = firstLine.split()

    def conn_destnation(self):
        url = urlparse.urlparse(self.headers['path'])
        hostname = url[1]
        port = "80"
        if hostname.find(':') > 0:
            addr, port = hostname.split(':')
        else:
            addr = hostname
        port = int(port)
        ip = socket.gethostbyname(addr)
        print ip, port
        self.destnation.connect((ip, port))
        data = "%s %s %s\r\n" % (self.headers['method'], self.headers['path'], self.headers['protocol'])
        self.destnation.send(data + self.request)
        print data + self.request
        if 'Cookie' in self.request:
            tmp_list = self.request.split('Cookie:')
            pre_req_list = tmp_list[0].rstrip('\r\n').split('\r\n')
            last_req_list = ['Cookie:'+tmp_list[1].rstrip('\r\n')]
        else:
            raise Exception('Other request type !')
        req_dic = {}
        for i in pre_req_list + last_req_list:
            req_dic.update({i.split(':')[0]: i.split(':')[1]})
        vals = {
            'id': 1,
            'name': ip + ':' + str(port),
            'method': self.headers['method'],
            'address': self.headers['path'],
            'cookie':req_dic.get('Cookie'),
            'accept':req_dic.get('Accept'),
        }
        db = DBHandler()
        db.create('test1')
        db.write(vals)
        db.close()

    def renderto(self):
        readsocket = [self.destnation]
        while True:
            data = ''
            (rlist, wlist, elist) = select.select(readsocket, [], [], 3)
            if rlist:
                data = rlist[0].recv(BUFLEN)
                if len(data) > 0:
                    self.source.send(data)
                else:
                    break

    def run(self):
        self.get_headers()
        self.conn_destnation()
        self.renderto()


class Server(object):
    def __init__(self, host, port, handler=Proxy):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(5)
        self.handler = handler

    def start(self):
        while True:
            try:
                lock = thread.allocate_lock()
                lock.acquire()
                conn, addr = self.server.accept()
                thread.start_new_thread(self.handler, (conn, addr, lock))
                while True:
                    if not lock.locked():
                        break
                print "lock release\n------------------------------------\n"
            except:
                pass


if __name__ == '__main__':
    s = Server('127.0.0.1', 8080)
    s.start()
