import socket
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.bind(("localhost", 9999))

msg , addr = s.recvfrom(1024)
print("CLient : ",msg.decode())

s.sendto("Hello from the server !! ".encode(),addr)
s.close()