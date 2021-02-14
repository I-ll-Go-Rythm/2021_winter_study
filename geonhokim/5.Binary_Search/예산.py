class Solution:
    def budget(self):
        N = int(input())
        requests = list(map(int, input().split()))
        budget_ = int(input())

        if sum(requests) <= budget_:
            return max(requests)

        low, heigh = 0, max(requests)

        while low + 1 < heigh:
            mid = (low + heigh) // 2

            sum_ = 0
            for req in requests:
                if req < mid:
                    sum_ += req
                else:
                    sum_ += mid

            
            if sum_ <= budget_:
                low = mid
            
            else:
                heigh = mid
        
        return low

sol = Solution()

print(sol.budget())