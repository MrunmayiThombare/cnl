import socket
s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)

c, addr = s.accept()
msg = c.recv(1024).decode()
a,b = map(int,msg.split())
result = a+b
c.send(str(result).encode())
c.close()
s.close()



 
