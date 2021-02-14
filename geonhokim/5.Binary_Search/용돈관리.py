class Solution:
    def manage(self) -> int:
        N, M = map(int, input().split())
        dayMoney = []

        for _ in range(N):
            dayMoney.append(int(input()))

        low, heigh = 0, sum(dayMoney)

        while low + 1 < heigh:
            mid = (low + heigh) // 2

            if mid < max(dayMoney):
                low = mid
                continue

            cnt = 0
            sum_ = 0
            for i in range(len(dayMoney)):
                sum_ += dayMoney[i]
                
                if sum_ > mid:
                    sum_ = dayMoney[i]
                    cnt += 1
                
            if cnt < M:
                heigh = mid
            else:
                low = mid
        
        return heigh



sol = Solution()
print(sol.manage())