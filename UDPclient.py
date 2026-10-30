import socket
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.sendto(input("Enter a string : ").encode(),("localhost",9999))

msg, recv = s.recvfrom(1024)
print("Uppercase : ",msg.decode())
s.close()
