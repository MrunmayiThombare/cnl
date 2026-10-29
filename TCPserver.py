import socket
s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)

c, addr = s.accept()
msg = c.recv(1024).decode()
print("client : ",msg)
c.send("Hello from the server !!".encode())
c.close()
s.close()
 