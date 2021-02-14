class Solution:
    def installRouter(self):
        N, C = map(int, input().split())
        houses = []
        for _ in range(N):
            houses.append(int(input()))

        houses.sort()
        low, heigh = 0, houses[-1] - houses[0]

        C = C - 1
        if C == 1:
            return heigh

        while low + 1 < heigh:
            mid = (low + heigh) // 2
            start = 0
            cnt = 0
            for _ in range(C):
                is_possible = False
                for i in range(start + 1, len(houses)):
                    if houses[i] - houses[start] >= mid:
                        start = i
                        is_possible = True
                        cnt += 1
                        break
            
            if cnt == C:
                is_possible = True
            else:
                is_possible = False
                
            if is_possible:
                low = mid
            else:
                heigh = mid

        return low

sol = Solution()
print(sol.installRouter())
