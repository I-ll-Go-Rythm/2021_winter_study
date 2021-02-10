#이거는 가장 긴 증가 부분 수열을 찾는 lis 알고리즘
# 반례 10 90 20 80 100

from typing import List

class Solution:
    def lis(self, numList: List[int]):
        dp = [num for num in numList]
        max_ = 0

        for i in range(1, len(numList)):
            for j in range(1, i):
                if (numList[j] < numList[i] and dp[i] < dp[j] + numList[i]):
                    dp[i] = dp[j] + numList[i]

            max_ = max(max_, dp[i])
        
        print(dp)
        return max_


n = int(input())

numList = [0] + list(map(int, input().split()))

sol = Solution()
print(sol.lis(numList))