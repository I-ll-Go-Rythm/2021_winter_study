import sys

N, K = map(int, input().split())
stuff = [[0, 0]]
knap = [[0 for _ in range(K + 1)] for _ in range(N+1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w = stuff[i][0]
        v = stuff[i][1]

        if j<w:
            knap[i][j] = knap[i-1][j]
        else:
            knap[i][j] = max(v +knap[i-1][j-w], knap[i-1][j])
print(knap[N][K])
