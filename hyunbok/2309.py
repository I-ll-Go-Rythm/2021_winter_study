a = []
a = [int(input()) for _ in range(9)]

a.sort()
result = sum(a)
for i in range(9):
    for j in range(i+1, 9):
        if result - a[i] - a[j] ==100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(a[k])
            exit()
