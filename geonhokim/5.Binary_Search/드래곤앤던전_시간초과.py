class Solution:
    def game(self):
        N, Hatk = map(int, input().split())
        dungeon = []
        for _ in range(N):
            T, Atk, HP = map(int, input().split())
            dungeon.append([T, Atk, HP])
        

        lowHP, heighHP = 1, 1000000000001

        while lowHP + 1 < heighHP:
            maxHP = (lowHP + heighHP) // 2
            curHP = maxHP
            winOrLose = True
            Hatk_ = Hatk
            for room in dungeon:
                T, Atk, HP = room[0], room[1], room[2]
                if T == 1:
                    if HP % Hatk: #나누어 떨어지지 않는 경우
                        if curHP - Atk * (HP // Hatk_) <= 0:
                            winOrLose = False
                            break
                        else:
                            curHP -= Atk * (HP // Hatk_)

                    else:
                        if curHP - Atk * ((HP // Hatk_) - 1) <= 0:
                            winOrLose = False
                            break
                        else:
                            curHP -= Atk * ((HP // Hatk_) - 1)

                else:
                    Hatk_ += Atk
                    if curHP + HP < maxHP:
                        curHP += HP
                    else:
                        curHP = maxHP
                    
            
            if winOrLose:
                heighHP = maxHP
            else:
                lowHP = maxHP

        return heighHP

sol = Solution()
print(sol.game())