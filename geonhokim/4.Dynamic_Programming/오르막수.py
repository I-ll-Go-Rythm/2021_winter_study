from typing import List
import sys
sys.setrecursionlimit(100000)

class Solution:
    def __init__(self, dp: List[int]):
        self.dp = dp

    def ascending(self, num: int, digit: int):
        cnt = 0
        if self.dp[num][digit]:
            return self.dp[num][digit]

        if digit == 1:
            self.dp[num][digit] = 1
            return 1

        if digit == 2:
            self.dp[num][digit] = 10 - num
            return 10 - num

        for nextNum in range(num, 10):
            self.dp[num][digit-1] = self.ascending(nextNum, digit - 1)
            cnt += self.dp[num][digit-1]
        
        self.dp[num][digit] = cnt

        return cnt


N = int(input())

dp = [[0 for _ in range(N + 1)] for _ in range(10)]

sol = Solution(dp)

sum = 0
for num in range(0, 10):
    sum += sol.ascending(num, N)

print(sum % 10007)