# 이런거 어떻게 생각해냐..

# 01 KnapSack 문제 많이 풀어보는 수밖에

# 코드 이해가 안되면 실제 내가 짐을 꾸려야하는 상황에 있다 생각하고
# 표를 그리면 이해 잘된다.
 
from typing import List

class Solution:
    def __init__(self, dp: List[int]):
        self.dp = dp

    def backPack(self, N: int, K: int):
        loads = [[0, 0]]

        for _ in range(N):
            weight, value = map(int, input().split())
            loads.append([weight, value])

        # i, N -> 몇번째?
        # j, K -> 무게
        for i in range(1, N + 1):
            weight = loads[i][0]
            value = loads[i][1]

            for j in range(K + 1):
                if loads[i][0] > j: # i번째 무게가 j(무게인덱스)보다 크다면 (배낭 무게 한도 초과)
                    self.dp[i][j] = self.dp[i-1][j] # 그 전차례 해당 무게인덱스의 value를 가져온다.
                
                else:
                    self.dp[i][j] = max(self.dp[i-1][j], self.dp[i-1][j-weight] + value)
        print(self.dp)
        return self.dp[N][K]

N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N + 1)]

sol = Solution(dp)
print(sol.backPack(N, K))