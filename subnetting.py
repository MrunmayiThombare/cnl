import ipaddress
ip = input("Enter the ip address : ")
a = int(ip.split(".")[0].split("/")[0])

if a>=1 and a<=126:
    c = "A"
elif a>=127 and a<=191:
    c = "B"
elif a>=192 and a<=223:
    c = "C"
else :
    c = "invalid"

if "/" not in ip:
    if c == "A":
        p = 8
    elif c == "B":
        p = 16
    elif c == "C":
        p = 24
    else :
        p = 24
    ip = ip + "/" + str(p)
net = ipaddress.IPv4Network(ip,strict = False)

print("Class : ",c)
for s in net.subnets(new_prefix = net.prefixlen+1):
    print("Subnet mask : ",s.netmask)
    print("Network : ",s.network_address)
    print("Total hosts : ",s.num_addresses - 2)
