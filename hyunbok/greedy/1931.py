<<<<<<< HEAD
num = int(input())
start = []
end = []
substract = []

for _ in range(num):
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)

for _ in range(len(start)):
    substract.append(end[_]-start[_])

temp = 0
if 
=======
N = int(input())
a = []
for _ in range(N):
    m, n = map(int, input().split())
    a.append([m, n])

a = sorted(a, key=lambda x:(x[1], x[0]))
last = 0 
ans = 0
for i, j in a:
    if i>=last:
        last = j
        ans ++1
>>>>>>> 0d317a691d9eb22032e11e6ff1579e3070b7e217
