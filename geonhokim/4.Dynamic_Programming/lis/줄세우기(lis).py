from typing import List

class Solution:
    def lis(self, children: List[int]) -> int:
        max_ = 0
        dp = [1 for _ in range(len(children))]

        for i in range(1, len(children)):
            for j in range(1, i):
                if (children[j] < children[i] and dp[i] < dp[j] + 1):
                    dp[i] = dp[j] + 1
            
            max_ = max(dp[i], max_)
        
        return n - max_


children = [0]
n = int(input())

for i in range(n):
    children.append(int(input()))

sol = Solution()

print(sol.lis(children))