import sys
n = int(sys.stdin.readline())
g = [list(map(str, input()))for _ in range(n)]
ans = 0

def funct(g):
    cnt = 0
    for i in range(n):
        row = 1
        col = 1
        for j in range(n-1):
            if g[i][j] == g[i][j+1]:
                row += 1
            else:
                cnt = max(cnt, row)
                row = 1
            if g[j][i] == g[j+1][i]:
                col += 1
            else:
                cnt = max(cnt, col)
                col = 1
        cnt = max(cnt, row, col)
    return cnt

for i in range(n):
    for j in range(n-1):
        if g[i][j]!=g[i][j+1]:
            tmp = g[i][j]
            g[i][j] = g[i][j+1]
            g[i][j+1] = tmp

            ans = max(ans, funct(g))

            tmp = g[i][j]
            g[i][j] = g[i][j+1]
            g[i][j+1] = tmp

        if g[j][i]!=g[j+1][i]:
            tmp = g[j][i]
            g[j][i] = g[j+1][i]
            g[j+1][i] = tmp
            ans = max(ans, funct(g))
            tmp = g[j][i]
            g[j][i] = g[j+1][i]
            g[j+1][i] = tmp
            
print(ans)
