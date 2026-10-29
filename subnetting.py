import ipaddress
ip = input("Enter the ip aaddress : ")
a = int(ip.split(".")[0].split("/")[0])

if a >= 1 and a<= 126 : 
    c = "A"

elif a >= 127 and a <= 191 :
    c = "B"

elif a >= 192 and a <= 223 :
    c = "C"

elif a >= 224 and a <= 239 :
    c = "D"

elif a >= 240 and a <= 255 :
    c = "E"

else : 
    c = "invalid"

if "/" not in ip :
    if c == "A" :
        p = 8

    elif c == "B" :
        p = 16

    elif c == "C" :
        p = 24

    else : 
        p = 24
        ip = ip + "/" + str(p)

net = ipaddress.IPv4Network(ip,strict = False)

print("Class : ",c)
print("Network address : ", net.network_address)
print("Subnet mask : ", net.netmask)
print("Broadcast address : ", net.broadcast_address)
print("First host : ", net.network_address + 1)
print("Last host : ", net.broadcast_address - 1)
print("Total host : ", max(net.num_addresses -2, 0))
