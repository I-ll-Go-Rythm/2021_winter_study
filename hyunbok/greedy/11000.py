N = int(input())
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

