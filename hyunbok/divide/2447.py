
def sol(x, y, N):
    if N != 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                sol(x + i*(N//3), y + j*(N//3), N//3)
        return
    else:
        for a in range(3):
            for b in range(3):
                if a==1 and b==1:
                    continue
                else:
                    m[x+a][y+b] = 1

N = int(input())

m = [[0 for i in range(N)] for i in range(N)]

sol(0, 0, N)

for x in range(N):
    for y in range(N):
        if m[x][y] == 1:
            print('*', end ='')
        else:
            print(' ', end ='')
    print()




