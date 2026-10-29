n = int(input("Enter the routers : "))
c = [list(map(int, input().split())) for i in range(n)]
d = [r[:] for r in c]

while True : 
    change = 0
    for i in range (n) : 
        for j in range(n) :
            for k in range(n): 
                if d[i][j] > c[i][k] + d[k][j] :
                    d[i][j] = c[i][k] + d[k][j]
                    change = 1
    if change == 0 :
            break

    for r in d: 
        print(r)

