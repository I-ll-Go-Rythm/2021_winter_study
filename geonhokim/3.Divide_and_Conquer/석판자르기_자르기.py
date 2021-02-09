from typing import List

class Solution:
    def __init__(self, slate: List[List[int]], n: int):
        self.slate = slate

    def cutting(self, si: int, sj: int, ei: int, ej: int, direction: int):
        if si >= ei and sj >= ej:
            return
        
        for ii in range(si, ei + 1):
            for jj in range(sj, ej + 1):
                print(self.slate[ii][jj], end=' ')
            print()
        print("--------------------")

        if not direction: # 가로자르기
            for ii in range(si, ei + 1):
                for jj in range(sj, ej + 1):
                    if self.slate[ii][jj] == 1 and sum(self.slate[ii]) == 1: # 하나씩 돌면서 불순물을 발견하면 (+ 거기에 결정체가 없으면)
                        self.cutting(si, sj, ii - 1, ej, 1)
                        self.cutting(ii + 1, sj, ei, ej, 1)

        
        if direction: # 세로자르기
            for ii in range(si, ei + 1):
                for jj in range(sj, ej + 1):
                    if self.slate[ii][jj] == 1:
                        flag = True
                        for x in range(ii + 1, ei + 1):
                            if self.slate[x][jj] == 2:
                                flag = False
                                break

                        if flag:
                            self.cutting(si, sj, ei, jj - 1, 0)
                            self.cutting(si, jj + 1, ei, ej, 0)

        return

n = int(input())
# slate = [[] for _ in range(n)]
# for i in range(n):
#     slate[i] = list(map(int, input().split()))
slate = [
[0, 0, 0, 0, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 2, 1, 0, 0, 2, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 2, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 2, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]


print("--------------------")

sol = Solution(slate, n)

sol.cutting(0, 0, n - 1, n - 1, 0)
sol.cutting(0, 0, n - 1, n - 1, 1)