# 1. 무게1, 가치3 인 짐을 계속해서 담을 수 없기 때문에 안된다.
# 2. 역시 짐의 무게를 더해가는데 무게4짜리를 더한거에 한번 더 더하는 계산이 발생한다.

from typing import List

class Solution:
    def __init__(self, dp: List[int]):
        self.dp = dp

    def backPack(self, N: int, K: int):
        load = []
        for _ in range(N):
            W, V = map(int, input().split())
            load.append((W, V))

        load.sort(key = lambda x: (x[0], x[1]))

        for weight, value in load:
            
            for i in range(1, K + 1):
                if i + weight >= K + 1:
                    break
                
                if i == weight:
                    self.dp[i] = max(value, self.dp[i])
                    continue

                if self.dp[i] == -1:
                    continue

                if self.dp[i] != -1:
                    self.dp[i + weight] = max(self.dp[i] + value, self.dp[i + weight])
                

        print(self.dp)
        return max(self.dp)




N, K = map(int, input().split())

dp = [0] + [-1 for _ in range(K)]

sol = Solution(dp)

print(sol.backPack(N, K))