i = 1
a = []

while True:
    l, p, v = map(int, input().split())
    if l+p+v == 0: break
    temp = v//p*l
    temp += min(v%p, l)
    a.append(temp)

for i in range(len(a)):
    print('Case', i+1, ':', a[i])

