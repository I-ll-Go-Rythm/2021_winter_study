import sys
sys.setrecursionlimit(1000000)

class Solution:
    def __init__(self, dp):
        self.dp = dp

    def binomial(self, N: int, K: int) -> int:
        if self.dp[N][K]:
            return self.dp[N][K]

        if K == 1:
            self.dp[N][K] = N
            return self.dp[N][K]

        if K == N or K == 0:
            self.dp[N][K] = 1
            return self.dp[N][K]

        self.dp[N][K] = self.binomial(N - 1, K - 1) + self.binomial(N - 1, K)
        return self.dp[N][K]%10007


N, K = map(int, input().split())
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
sol = Solution(dp)

print(sol.binomial(N, K))