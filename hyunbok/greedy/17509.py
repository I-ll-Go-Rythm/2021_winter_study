D = []
V = []
for i in range(11):
    d, v = map(int, input().split())
    D.append(d)
    V.append(v)
D.sort()
temp = []
stack = 0
for i in D:
    temp.append(stack+i)
    stack = stack + i
print(sum(temp)+sum(V)*20)
