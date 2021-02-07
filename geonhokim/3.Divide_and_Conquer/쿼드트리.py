from typing import List

class Solution:
    def __init__ (self, video: List[int]):
        self.video = video
        self.result = []

    def QuadTree (self, i: int, j: int, n: int):
        if n == 1:
            # self.type[self.video[i][j]] += 1
            self.result.append(self.video[i][j])
            # print(f"{self.video[i][j]}이 1만큼 오름")
            return

        flag = True
        for ii in range(i, i + n):
            for jj in range(j, j + n):
                # print(ii, jj)
                if self.video[ii][jj] != self.video[i][j]:
                    flag = False
                    break

        if flag:
            self.result.append(self.video[i][j])
            # print(f"{self.video[i][j]}이 1만큼 오름")
            return

        else:
            self.result.append('(')
            for ii in range(i, i + n, n//2):
                for jj in range(j, j + n, n//2):
                    # print(ii, jj)
                    self.QuadTree(ii, jj, n//2)
            self.result.append(')')


        return
        


n = int(input())

video = [[] for _ in range(n)]

for i in range(n):
    video[i] = list(input())

# video = \
# [
# [1,1,1,1,0,0,0,0],
# [1,1,1,1,0,0,0,0],
# [0,0,0,1,1,1,0,0],
# [0,0,0,1,1,1,0,0],
# [1,1,1,1,0,0,0,0],
# [1,1,1,1,0,0,0,0],
# [1,1,1,1,0,0,1,1],
# [1,1,1,1,0,0,1,1]]
sol = Solution(video)


sol.QuadTree(0, 0, n)
# print(sol.result)

print(''.join(sol.result))