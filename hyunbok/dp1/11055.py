n = int(input())
g = list(map(int, input().split()))
m = [0 for i in range(n)]
m[0] = g[0]
for i in range(1, n):
    s = []
    for j in range(i-1, -1, -1):
        if g[i]>g[j]:
            s.append(m[j])
    if not s:
        m[i] = g[i]
    else:
        m[i] = g[i] + max(s)
print(max(m))

