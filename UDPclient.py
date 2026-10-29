import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(input("Message :").encode() , ("localhost",9999))

msg, addr = s.recvfrom(1024)
print("Client : ",msg.decode())
s.close()
