def sol(x):
    global ans
    if x == len(g):
        result = 1
        return
    if m[x]:
        return
    m[x] = 1
    for i in range(len(A)):
        if len(g[x:])>=len(A[i]):
            for j in range(len(A[i])):
                if A[i][j]!=g[x+j]:
                    break
            else:
                sol(x+len(A[i]))
    return
g = input()
A = []
m = [0]*101
for _ in range(int(input())):
    A.append(input())
ans = 0
sol(0)
print(ans)
