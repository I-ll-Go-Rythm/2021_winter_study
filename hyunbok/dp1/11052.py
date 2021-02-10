N = int(input())
m = [0]*(N+1)
p = [0]+list(map(int, input().split()))

m[1] = p[1]
for i in range(2, N+1):
    for j in range(0, i):
        if p[i-j]+p[j]>m[i]:
            m[i] = p[i-j]+p[j]
        if m[i-j]+m[j]>m[i]:
            m[i] = m[i-j]+m[j]
print(m[N])





