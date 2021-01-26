list = [20, 7, 23, 19, 10, 15, 25, 8, 13]
list.sort()
target = sum(list)-100
for i in range(0, 9):
    for j in range(0, 9):
        if i == j : 
            j+=1
            continue
        if list[i]+list[j]==target:
            del list[i]
            del list[j]
            print(list)


