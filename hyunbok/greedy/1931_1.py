a = [[1, 4], [3, 5], [3, 4], [2, 2], [1, 2]]

a.sort()

print(a)

a = [[1, 4], [3, 5], [3, 4], [2, 2], [1, 2]]

a = sorted(a, key = lambda x:x[0])

print(a)

a = [[1, 4], [3, 5], [3, 4], [2, 2], [1, 2]]

a = sorted(a, key = lambda x:(x[1], x[0]))

print(a)

a = [[1, 4], [3, 5], [3, 4], [2, 2], [1, 2]]

a = sorted(a, key = lambda x:(x[0], x[1]))

print(a)


a = [[1, 4], [3, 5], [3, 4], [2, 2], [1, 2]]

a = sorted(a, key = lambda x:x[0])
a = sorted(a, key = lambda x:x[1])

print(a)

