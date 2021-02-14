class Solution:
    def minBlueRay(self):
        N, M = map(int, input().split())
        lessons = list(map(int, input().split()))

        low, heigh = 0, sum(lessons)

        while low + 1 < heigh:
            blueRay = [0 for _ in range(M)]
            mid = (low + heigh) // 2

            sum_ = 0
            cnt = 0
            for i in range(len(lessons)):
                sum_ += lessons[i]

                if cnt == M - 1:
                    blueRay.append(sum(lessons[i:]))
                    break
                elif i == len(lessons) - 1:
                    blueRay.append(sum_)
                elif sum_ + lessons[i + 1] > mid:
                    blueRay.append(sum_)
                    cnt += 1
                    sum_ = 0

            if max(blueRay) <= mid:
                heigh = mid
            
            else:
                low = mid

        return heigh

sol = Solution()
print(sol.minBlueRay())