class Solution:
    def buyCard(self, N: int):
        dp = [0] * (N + 1)

        cardPacks = [0] + list(map(int, input().split()))

        for ea in range(1, len(cardPacks) + 1):
            for i in range(ea, N + 1):
                dp[i] = max(dp[i - ea] + cardPacks[ea], dp[i]) # cardPacks[ea] = price

        return dp[-1]

N = int(input())

sol = Solution()

print(sol.buyCard(N))