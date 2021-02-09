from typing import List

class Solution:
    def __init__(self, slate: List[List[int]], n: int):
        self.slate = slate
    
    def isAvailable(self, s: int, e: int, jj: int, ii: int, direction: int):
        if direction == 0:
            print(self.slate[ii][s:e + 1])
            print(sum(self.slate[ii][s:e + 1]))

            return sum(self.slate[ii][s:e + 1]) == 1

        else:
            for x in range(s, e + 1):
                if self.slate[x][jj] == 2:
                    return 0
            return 1

    def cutting(self, si: int, sj: int, ei: int, ej: int, direction: int):
        
        # 더 잘라도 되는가
        checkArray = [0, 0, 0]

        for ii in range(si, ei + 1):
            for jj in range(sj, ej + 1):
                checkArray[self.slate[ii][jj]] += 1
        
        if checkArray[2] == 1 and checkArray[1] == 0:
            return 1
        if checkArray[2] == 0:
            return 0
        ###

        # 확인용
        for ii in range(si, ei + 1):
            for jj in range(sj, ej + 1):
                print(self.slate[ii][jj], end=' ')
            print()
        print("--------------------")
        ###


        # 자르고 가능여부 더해가기
        cnt = 0
        for ii in range(si, ei + 1):
            for jj in range(sj, ej + 1):
                if self.slate[ii][jj] == 1:

                    if (direction == 0 and self.isAvailable(sj, ej, jj, ii, direction)):
                        cnt += self.cutting(si, sj, ii - 1, ej, 1) * self.cutting(ii + 1, sj, ei, ej, 1)
                    
                    elif (direction == 1 and self.isAvailable(si, ei, jj, ii, direction)):
                        cnt += self.cutting(si, sj, ei, jj - 1, 0) * self.cutting(si, jj + 1, ei, ej, 0)

        return cnt

n = int(input())
slate = [[] for _ in range(n)]
for i in range(n):
    slate[i] = list(map(int, input().split()))
# slate = [
# [0, 0, 0, 0, 0, 2, 0, 0],
# [0, 0, 0, 0, 0, 0, 1, 0],
# [0, 0, 2, 1, 0, 0, 2, 0],
# [0, 1, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 2, 1, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 2, 0],
# [0, 0, 0, 0, 0, 0, 0, 0]
# ]


print("--------------------")

sol = Solution(slate, n)

cnt = sol.cutting(0, 0, n - 1, n - 1, 0) + sol.cutting(0, 0, n - 1, n - 1, 1)

if cnt == 0:
    print(-1)
else:
    print(cnt)