#시간 초과
from typing import List

class Solution:
    def __init__(self, paper: List[List[int]]):
        self.paper = paper
        self.paperType = {
            -1: 0,
            0: 0,
            1: 0
        }

    def counting(self, i: int, j: int, n: int) -> int:
        if n == 1:
            self.paperType[self.paper[i][j]] += 1
            return

        flag = True
        for ii in range(i, i + n):
            for jj in range(j, j + n):
                if self.paper[ii][jj] != self.paper[i][j]:
                    flag = False
                    break
        
        if flag:
            self.paperType[self.paper[i][j]] += 1
            return
        
        else:

            for ii in range(i, i + n, n//3):
                for jj in range(j, j + n, n//3):
                    # print(ii, jj)
                    self.counting(ii, jj, n//3)

        return
        
n = int(input())

arr = [[]] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))


# arr = \
# [[0, 0, 0, 1, 1, 1, -1, -1, -1],
# [0, 0, 0, 1, 1, 1, -1, -1, -1],
# [0, 0, 0, 1, 1, 1, -1, -1, -1],
# [1, 1, 1, 0, 0, 0, 0, 0, 0],
# [1, 1, 1, 0, 0, 0, 0, 0, 0],
# [1, 1, 1, 0, 0, 0, 0, 0, 0],
# [0, 1, -1, 0, 1, -1, 0, 1, -1],
# [0, -1, 1, 0, 1, -1, 0, 1, -1],
# [0, 1, -1, 1, 0, -1, 0, 1, -1]]

sol = Solution(arr)

sol.counting(0, 0, n)
print(sol.paperType[-1])
print(sol.paperType[0])
print(sol.paperType[1])