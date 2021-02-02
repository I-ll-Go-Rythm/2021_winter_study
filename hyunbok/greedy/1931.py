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
