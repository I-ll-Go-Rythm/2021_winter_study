N = int(input())
g = [[1 for _ in range(11)] for _ in range(N+1)]
for _ in range(10):
    g[0].insert(1, 0)

for i in range(2, N+1):
    for j in range(0, 1):
        g[i][j] = g[i-1][j+1]
    for j in range(1, 9):
        g[i][j] = g[i-1][j+1] + g[i-1][j-1]
    for j in range(9, 10):
        g[i][j] = g[i-1][j-1]

print(sum(g[N][_] for _ in range(1, 10))%pow(10, 9))
