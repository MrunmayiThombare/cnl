d = input("Enter the binary data : ")
m = len(d)
r = 0

while 2**r < m+r+1:
    r += 1

n = m+r
h = ['0']*(n+1)
j = 0

for i in range(1,n+1):
    if i & i-1 :
        h[i] = d[j]
        j+=1

for i in range(r):
    p = 2**i
    for k in range(1,n+1):
        if k & p :
            h[p] = str(int(h[p]) ^ int(h[k]))

print("Hamming code : ",''.join(h[1:]))

pos = int(input("enter the position for error : "))
h[pos] = str(int(h[pos]) ^ 1)
print("Reeived data : ",''.join(h[1:]))
s = 0
for i in range(r):
    p = 2**i
    x = 0
    for k in range(1,n+1):
        x^= int(h[k])

    s += x*p

if s:
    h[s] = str(int(h[s]) ^ 1)
print("The corrected data : ", ''.join(h[1:]))
