N = int(input())
g = []
for I in range(N):
    g.append(list(map(int, input().split())))

a = 0
b = 0
c = 0

def sol(x, y, n):
    global a, b, c

    num_check = g[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if (g[i][j] != num_check):
                for k in range(3):
                    for l in range(3):
                        sol(x + k *n//3, y+l*n//3, n//3)
                return
    if(num_check == -1):
        a += 1
    elif(num_check == 0):
        b += 1
    else:
        c += 1

sol(0, 0, N)
print(f'{a}\n{b}\n{c}')




