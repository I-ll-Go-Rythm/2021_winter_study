from typing import List

class Solution:
    def __init__(self, stars: List[List[int]]):
        self.stars = stars

    def star(self, i: int, j: int, n: int):
        if n == 1:
            self.stars[i][j] = "*" 
            return
    

        for ii in range(i, i + n, n//3):
            for jj in range(j, j + n, n//3):

                if ii % n == 1 and jj % n == 1:
                    continue
                
                if ii % n == n//3 and jj % n == n//3:
                    continue

                self.star(ii, jj, n//3)



n = int(input().rstrip())

stars = [[" " for _ in range(n)] for _ in range(n)]

sol = Solution(stars)

sol.star(0, 0, n)


for i in range(n):
    for j in range(n):
        print(sol.stars[i][j], end='')
    print()
    #print("\n")로 하면 출력 형식이 잘못되었습니다!