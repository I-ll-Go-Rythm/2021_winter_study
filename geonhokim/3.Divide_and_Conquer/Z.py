from typing import List

class Solution:
    def __init__(self, r: int, c: int):
        self.index = 0
        self.r = r
        self.c = c
        self.flag = False

    def Zsearch(self, i: int, j: int, n: int):
        if n == 2:
            for ii in range(i, i + 2):
                for jj in range(j, j + 2):
                    if ii == self.r and jj == self.c:
                        print(self.index)
                        self.flag = True
                        return
                        
                    self.index += 1
            
            return

        
        for ii in range(i, i + n, n//2):
            if self.flag:
                break
            for jj in range(j, j + n, n//2):
                if self.flag:
                    break
                if ii // (n // 2) < self.r // (n // 2) or jj // (n // 2) < self.c // (n // 2):
                    self.index += (n//2) ** 2
                    continue

                self.Zsearch(ii, jj, n//2)
        
        return


N, r, c = map(int, input().split())

sol = Solution(r, c)

sol.Zsearch(0, 0, 2 ** N)