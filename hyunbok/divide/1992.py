N = int(input())
g = []
for _ in range(N):
    g.append(list(map(int, input())))

def sol(x, y, N):
    num_check = g[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if g[i][j] != num_check:
                return ('(%s%s%s%s)' % (sol(x, y, N//2), sol(x, y+N//2, N//2), sol(x+N//2, y, N//2), sol(x+N//2, y+N//2, N//2)))
    if num_check == 1:
        return ('%d' % (num_check))
    else:
        return ('%d' % (0))

print(sol(0, 0, N))

