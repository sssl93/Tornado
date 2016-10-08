import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',9999))
s.listen(5)
while True:
    conn,addr = s.accept()
    buf = s.recv(1024)
    print buf