k = int(input())
list = []
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if 101*a+11*b+2*c == k:
                list.append(100*a+10*b+c)
print(min(list))


