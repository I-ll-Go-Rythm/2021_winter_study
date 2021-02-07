m, n = map(int, input().split())
g = []
g = [input() for _ in range(m)]
collection = []

for a in range(m - 7):
    for x in range(n - 7):
        temp1=0
        temp2=0
        for b in range(a, a+8):
            for y in range(x, x+8):
                if (b+y)%2 == 0:
                    if g[b][y]!='W':
                        temp1 +=1
                    if g[b][y]!='B':
                        temp2 +=1
                else:
                    if g[b][y]!='B':
                        temp1 += 1
                    if g[b][y]!='W':
                        temp2 +=1
        collection.append(temp1)
        collection.append(temp2)
print(min(collection))

