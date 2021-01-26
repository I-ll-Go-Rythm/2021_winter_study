a = input()
b = int(a)
g = [input() for _ in range(b)]

for i in range(0, a):
    for j in range(0, a-1):
        temp = g[j][i]
        g[j][i] = g[j+1][i]
        g[j+1][i] = temp



from itertools import groupby
def long_repeat(data):
    return max([len(list(g)) for k, g in groupby(data)], default = 0)

for i in range(0, a):
    for j in range(0, a):
        list.append(long_repeat(g[i][j]))
        list.append(long_repeat(g[j][i]))
max(list)
