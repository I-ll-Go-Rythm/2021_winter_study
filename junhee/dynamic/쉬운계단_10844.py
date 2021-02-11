def stair(n,s):
    if dp[n][s] != 0:
        return dp[n][s]
    if n == 1 :
        return 1
    elif s == 0:
        dp[n][s] = stair(n-1,s+1)
        return dp[n][s]
    elif s == 9:
        dp[n][s] = stair(n-1,s-1)
        return dp[n][s]
    else:
        dp[n][s] = stair(n-1,s-1)+stair(n-1,s+1)
        return dp[n][s]
N = int(input())
answer = 0
dp = [[0 for _ in range(10)]for _ in range(N+1)]


for i in range(1,10):
    answer += stair(N,i)
print(answer)