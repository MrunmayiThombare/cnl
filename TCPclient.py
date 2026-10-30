import socket
s = socket.socket()
s.connect(("localhost",9999))

a = int(input("Enter no a : "))
b = int(input("Enter no b : "))
s.send(f"{a},{b}".encode())
result = a + b
print("Addition : ",s.recv(1024).decode())
s.close()
