from itertools import combinations

array = []

for i in range(9):
    a = input()
    array.append(int(a))

array.sort()
Sum = sum(array)
imposter = combinations(array, 2)

for a, b in list(imposter):
    if Sum - (a+b) == 100:
        break

for i in array:
    if i != a and i != b:
        print(i)