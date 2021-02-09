import sys


class Solution:
    def __init__(self, dp):
        self.dp = dp

    def makeToOne(self, X: int):
        if X == 1:
            return self.dp[X]
            # return 1
        
        if self.dp[X]:
            return self.dp[X]

        else:
            result = self.makeToOne(X-1) + 1
            
            if X % 3 == 0:
                result = min(self.makeToOne(X//3) + 1, result)

            if X % 2 == 0:
                result = min(self.makeToOne(X//2) + 1, result)
            
            self.dp[X] = result
            return self.dp[X]


N = int(input())
dp = [0] * (N + 1)
sys.setrecursionlimit(10000001)

sol = Solution(dp)

print(sol.makeToOne(N))