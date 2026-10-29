import socket
s = socket.socket()
s.connect(("localhost",9999))

s.send(input("Message : ").encode())
print("Client : ",s.recv(1024).decode())
s.close()