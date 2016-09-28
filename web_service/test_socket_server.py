# coding:utf-8
# 创建SocketServerTCP服务器：
import SocketServer
from SocketServer import StreamRequestHandler as SRH
from time import ctime

host = '127.0.0.1'
port = 9999
addr = (host, port)
RSTR = '''HTTP/1.1 200 OK
Proxy-Connection: Keep-Alive
Connection: Keep-Alive
Content-Length: 8296
Via: 1.1 JA-ISA02
Expires: Fri, 18 May 2012 09:05:56 GMT
Date: Fri, 18 May 2012 09:05:56 GMT
Content-Type: text/html;charset=gb2312
Server: BWS/1.0
Cache-Control: private

test'''


class Servers(SRH):
    def handle(self):
        print 'got connection from ', self.client_address
        self.wfile.write('connection %s:%s at %s succeed!' % (host, port, ctime()))
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print data
            print "RECV from ", self.client_address[0]
            import datetime
            now = str(datetime.datetime.now())
            print now
            self.request.sendall('HTTP/1.1 200 OK')
            self.connection.close()
            break


if __name__ == '__main__':
    print 'server is running....'
    server = SocketServer.ThreadingTCPServer(addr, Servers)
    server.serve_forever()
