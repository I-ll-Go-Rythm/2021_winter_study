class Solution:
    def squareNum(self, N: int) -> int:
        dp = [0] + [100001 for i in range(1, N + 1)]

        for num in range(1, int(N ** 0.5) + 1):
            sqNum = num ** 2

            for i in range(sqNum, N + 1):
                dp[i] = min(dp[i], dp[i-sqNum] + 1)

        return dp[-1]

N = int(input())

sol = Solution()
print(sol.squareNum(N))