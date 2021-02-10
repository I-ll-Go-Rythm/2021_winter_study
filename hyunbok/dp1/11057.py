N = int(input())
g = [[0 for _ in range(10)] for _ in range(N+1)]

for _ in range(10):
    g[1].insert(0, 1)

for i in range(2, N+1):
    for j in range(10):
        g[i][j] = sum(g[i-1][_] for _ in range(j, 10))

print(sum(g[N][_] for _ in range(10))%10007)
