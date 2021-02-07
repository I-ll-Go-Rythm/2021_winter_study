N = int(input())
a = []
for _ in range(N):
    m, n = map(int, input().split())
    a.append([m, n])

a = sorted(a, key=lambda x:(x[0], x[1]))
last = 0 
ans = 0
for i, j in a:
    if i>=last:
        last = j
        ans += 1
print(ans)
