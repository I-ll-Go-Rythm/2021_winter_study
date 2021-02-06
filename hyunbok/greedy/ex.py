a = []
for _ in range(11):
    m, n = map(int, input().split())
    a.append([m, n])
a = sorted(a, key = lambda x:(x[1], x[0]))
print(a)
