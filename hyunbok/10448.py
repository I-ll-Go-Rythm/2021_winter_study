a= input()
b = int(a)
g = [input() for i in range(0, b)]
tri_num = []
ans = {}

for i in range(0, 50):
    tri_num.append((i*(i+1)/2))
for j in range(0, b):
    for x in tri_num: 
        for y in tri_num:
            for z in tri_num:
                if x+y+z == g[j]:
                    ans[j] = 1
                else: ans[j] = 0
for k in n:
    print(k)
