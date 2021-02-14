class Solution:
    def cutLAN(self):
        K, N = map(int, input().split())
        LANs = []
        
        for _ in range(K):
            LANs.append(int(input()))
        
        low, heigh = 0, max(LANs) + 1  # 다른 문제들과 다른점, 항상 생각하고 넘어가야 한다.

        while low + 1 < heigh:
            mid = (low + heigh) // 2
            
            sum_ = 0
            for l in LANs:
                sum_ += l // mid
            
            if sum_ < N:
                heigh = mid
            else:
                low = mid
        
        return low


sol = Solution()
print(sol.cutLAN())