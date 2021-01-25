def MaxNum(a):
    chain = 1
    maxchain = 1
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            chain += 1
            if i+1 == len(a)-1:
                if maxchain < chain:
                    maxchain = chain
        else:
            if maxchain < chain:
                maxchain = chain
            chain = 1
    return maxchain

n = int(input())
array = []

for i in range(n):
    string = list(input())
    array.append(string)

firstmax = 1

temp=1

for i in range(n):
    for j in range(n-1):
        (array[i][j],array[i][j+1])=(array[i][j+1],array[i][j])
        temp = MaxNum(array[i])
        if temp > firstmax:
            firstmax = temp
        array = list(map(list,zip(*array)))
        temp = MaxNum(array[j])
        if temp > firstmax:
            firstmax = temp
        temp = MaxNum(array[j+1])
        if temp > firstmax:
            firstmax = temp
        array = list(map(list,zip(*array)))
        (array[i][j+1],array[i][j])=(array[i][j],array[i][j+1])

array = list(map(list,zip(*array)))

temp=1

for i in range(n):
    for j in range(n-1):
        (array[i][j],array[i][j+1])=(array[i][j+1],array[i][j])
        temp = MaxNum(array[i])
        if temp > firstmax:
            firstmax = temp
        array = list(map(list,zip(*array)))
        temp = MaxNum(array[j])
        if temp > firstmax:
            firstmax = temp
        temp = MaxNum(array[j+1])
        if temp > firstmax:
            firstmax = temp
        array = list(map(list,zip(*array)))
        (array[i][j+1],array[i][j])=(array[i][j],array[i][j+1])
print(firstmax)