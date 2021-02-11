import sys; sys.setrecursionlimit(1500)
def ormak(n,s):
    if dp[n][s] != 0:
        return dp[n][s]
    if n == 1 :
        return 1
    else:
        for i in range(s, 10):
            dp[n][s] += ormak(n-1,i)
        return dp[n][s]
N = int(input())
answer = 0
dp = [[0 for _ in range(10)]for _ in range(N+1)]

for i in range(10):
    answer += ormak(N,i)
print(answer%10007)