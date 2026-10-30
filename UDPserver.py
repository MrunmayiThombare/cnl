import socket
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.bind(("localhost",9999))
msg, addr = s.recvfrom(1024)
print("Client : ",msg.decode())
s.sendto(msg.decode().upper().encode() , addr)
s.close()
