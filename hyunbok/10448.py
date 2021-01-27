tri = [n*(n+1)//2 for n in range(1, 46)]
eur = [0] * 1001

for a in tri:
    for b in tri:
        for c in tri:
            if a+b+c<=1000:
                eur[a+b+c] = 1
x = int(input())
k = []
for i in range(x):
    k.append(eur[int(input())])
for _ in range(len(k)):
    print(k[_])

