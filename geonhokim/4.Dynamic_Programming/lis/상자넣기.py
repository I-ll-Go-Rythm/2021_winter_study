from typing import List

class Solution:
    def lis(self, box: List[int]) -> int:
        max_ = 0
        dp = [1 for _ in range(len(box))]

        for i in range(1, len(box)):
            for j in range(1, i):
                if (box[j] < box[i] and dp[i] < dp[j] + 1): # lis의 핵심 아이디어
                    dp[i] = dp[j] + 1
            
            max_ = max(dp[i], max_)
        
        return max_

n = int(input())
box = [0] + list(map(int, input().split()))

sol = Solution()

print(sol.lis(box))