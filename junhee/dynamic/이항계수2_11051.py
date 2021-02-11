import sys; sys.setrecursionlimit(1500)
def com(n,k):
    if k == 0 or n == k:
        return 1
    
    elif dp[n][k] != 0:
        return dp[n][k]
    dp[n][k] = com(n-1,k-1)+com(n-1,k)
    return dp[n][k]

N, K = map(int, input().split())
dp = [[0 for _ in range(N+1)]for _ in range(N+1)]

print(com(N,K)%10007)