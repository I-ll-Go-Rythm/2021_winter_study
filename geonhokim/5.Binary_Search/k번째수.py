class Solution:
    def Kth(self):
        N, K = int(input()), int(input())
        low, high = 0, K

        while low + 1 <= high:
            mid = (low + high) // 2
            
            min_ = 0
            for i in range(1, N + 1):
                min_ += min(mid // i, N) 
            
            if min_ >= K: 
                high = mid 
            else:
                low = mid 

    
        return high

sol = Solution()
print(sol.Kth())