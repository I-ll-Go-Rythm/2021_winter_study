from typing import List

class Solution:
    def lis(self, numList: List[int]):
        dp = [[1, num] for num in numList]
        max_ = 0

        for i in range(1, len(numList)):
            for j in range(1, i):
                if (numList[j] < numList[i] and dp[i][0] < dp[j][0] + 1):
                    dp[i][0] = dp[j][0] + 1
                    dp[i][1] += numList[j]

            max_ = max(max_, dp[i][1])
        
        print(dp)
        return max_


n = int(input())

numList = [0] + list(map(int, input().split()))

sol = Solution()
print(sol.lis(numList))