import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',9999))
c.send('1'.encode('utf-8'))
