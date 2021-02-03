N = int(input())
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
