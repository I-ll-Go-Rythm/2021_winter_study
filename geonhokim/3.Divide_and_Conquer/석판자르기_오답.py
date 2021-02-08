from typing import List

class Solution:
    def __init__(self, slate: List[List[int]], n: int):
        self.slate = slate
        self.n = n

    def cutting(self, i: int, j: int, ni: int, nj: int, direction: int):
        for ii in range(i, i + ni):
            for jj in range(j, j + nj):
                print(self.slate[ii][jj], end=' ')
            print()
        print("--------------------")

        if not direction: # 가로자르기
            for ii in range(i, i + ni):
                for jj in range(j, j + nj):
                    if self.slate[ii][jj] == 1 and sum(self.slate[ii]) == 1: # 하나씩 돌면서 불순물을 발견하면 (+ 거기에 결정체가 없으면)
                        self.cutting(i, j, ii - i, self.n - j, 1)
                        self.cutting(ii + 1, j, self.n - ii - 1, self.n - j, 1)

        
        if direction: # 세로자르기
            for ii in range(i, i + ni):
                for jj in range(j, j + nj):
                    if self.slate[ii][jj] == 1:
                        flag = True
                        for x in range(ii + 1, i + ni):
                            if self.slate[x][jj] == 2:
                                flag = False
                                break

                        if flag:
                            self.cutting(i, j, self.n - i, jj - j, 0)
                            self.cutting(i, jj + 1, self.n - i, self.n - jj - 1, 0)

        return

n = int(input())
slate = [[] for _ in range(n)]

for i in range(n):
    slate[i] = list(map(int, input().split()))
print("--------------------")

sol = Solution(slate, n)

sol.cutting(0, 0, n, n, 0)