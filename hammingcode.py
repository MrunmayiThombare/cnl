d = input("Enter binary data: ")
m = len(d)
r = 0

while 2**r < m+r+1:
    r += 1

n = m+r
h = ['0']*(n+1)
j = 0

for i in range(1,n+1) :
    if i & (i-1) : 
        h[i] = d[j]
        j += 1

for i in range (r) : 
    p = 2**i
    for k in range(1 , n+1) : 
        if k & p : 
            h[p] = str(int(h[p]) ^ int(h[k]))

code = ' '.join(h[1:])
print("Hamming code is : ", code)
