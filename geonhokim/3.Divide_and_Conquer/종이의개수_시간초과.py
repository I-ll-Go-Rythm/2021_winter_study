#시간 초과
from typing import List

class Solution:
    def __init__(self):
        self.M = 0
        self.Z = 0
        self.P = 0

    def counting(self, paper: List[int]) -> int:
        if sum(sum(paper, [])) == (len(paper) ** 2) * (-1):
            self.M += 1
            return
        if not any(sum(paper, [])):
            self.Z += 1
            return
        if sum(sum(paper, [])) == len(paper) ** 2:
            self.P += 1
            return


        n = len(paper)
        new = [[]] * (n//3)

        for j in range(0, n, n//3):
            for i in range(0, n, n//3):
                for k in range(n//3):
                    new[k] = paper[i+k][j:j+n//3]
                
                # print(new)
                self.counting(new)


sol = Solution()

# n = int(input())

# arr = [[]] * n
# for i in range(n):
#     arr[i] = list(map(int, input().split()))

arr = \
[[0, 0, 0, 1, 1, 1, -1, -1, -1],
[0, 0, 0, 1, 1, 1, -1, -1, -1],
[0, 0, 0, 1, 1, 1, -1, -1, -1],
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 1, -1, 0, 1, -1, 0, 1, -1],
[0, -1, 1, 0, 1, -1, 0, 1, -1],
[0, 1, -1, 1, 0, -1, 0, 1, -1]]
sol.counting(arr)

print(sol.M)
print(sol.Z)
print(sol.P)