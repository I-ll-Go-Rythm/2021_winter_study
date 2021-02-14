class Solution:
    def installRouter(self):
        N, C = map(int, input().split())
        houses = []
        for _ in range(N):
            houses.append(int(input()))

        houses.sort()
        low, heigh = 0, houses[-1] - houses[0] + 1

        C = C - 1
        if C == 1:
            return heigh - 1

        while low + 1 < heigh:
            mid = (low + heigh) // 2
            start = 0
            cnt = 0
            
            for i in range(1, len(houses)):
                if houses[i] - houses[start] >= mid:
                    start = i
                    cnt += 1
            
            if cnt >= C:
                low = mid
            else:
                heigh = mid
        
        return low


sol = Solution()
print(sol.installRouter())
