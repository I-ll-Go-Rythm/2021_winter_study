import sys

class Solution:
    def game(self):
        N, Hatk = map(int, input().split())

        curHP = 0
        maxHP = 0
        for _ in range(N):
            T, Atk, HP = map(int, sys.stdin.readline().split())  # 배열 선언해서 하면 시간초과 걸리니 sys.stdin ~ 사용할 것
            if T == 1:
                if HP % Hatk:
                    curHP -= Atk * (HP // Hatk)
                else:
                    curHP -= Atk * ((HP // Hatk) - 1)

            else:
                Hatk += Atk
                if curHP + HP < 0:
                    curHP += HP
                else:
                    curHP = 0
            
            maxHP = max(maxHP, -curHP)
                
        return maxHP + 1

sol = Solution()
print(sol.game())