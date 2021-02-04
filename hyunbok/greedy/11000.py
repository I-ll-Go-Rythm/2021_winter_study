N = int(input())
<<<<<<< HEAD
C = []
end = [0]

for i in range(N):
    C.append(list(map(int, input().split())))
C = sorted(C, key = lambda x :(x[0], x[1]))

for i in range(N):
    if C[i][0] >= min(end):
        end.remove(min(end))
        end.append(C[i][1])
    else:
        end.append(C[i][1])
print(len(end))

=======
a = []
end = [0]
for _ in range(N):
    m, n = map(int, input().split())
    a.append([m, n])

a = sorted(a, key = lambda x:(x[0],x[1]))

for i in range(N):
    if a[i][0]>=min(end):
        end.remove(min(end))
        end.append(a[i][1])
    else:
        end.append(a[i][1])
print(len(end))
>>>>>>> 0d317a691d9eb22032e11e6ff1579e3070b7e217
