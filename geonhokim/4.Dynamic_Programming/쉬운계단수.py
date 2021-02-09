from typing import List

class Solution:
    def __init__(self, dp: List[int]):
        self.dp = dp

    def stairsNum(self, num: int, digit: int):
        if self.dp[num][digit]:
            return self.dp[num][digit]

        if digit == 1:
            self.dp[num][digit] = 1
            return 1
        
        if num == 9:
            cnt = self.stairsNum(num - 1, digit - 1)
        elif num == 0:
            cnt = self.stairsNum(num + 1, digit - 1)
        else:
            cnt = self.stairsNum(num - 1, digit - 1) + self.stairsNum(num + 1, digit - 1)
        
        self.dp[num][digit] = cnt

        return cnt


N = int(input())

dp = [[0 for _ in range(N + 1)] for _ in range(10)]

sol = Solution(dp)

sum = 0

for num in range(1, 10):
    sum += sol.stairsNum(num, N)

print(sum % 1000000000)