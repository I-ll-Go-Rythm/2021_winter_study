import sys

class Solution:
    def hidingDTR(self):
        N, K, D = map(int, sys.stdin.readline().split())
        boxes = []

        for _ in range(K):
            A, B, C = map(int, sys.stdin.readline().split())
            boxes.append([A, B, C])
        
        low, high = 0, N + 1

        while low + 1 < high:
            mid = (low + high) // 2
            cnt = 0

            for box in boxes:
                start, end, gap = box[0], box[1], box[2]

                if mid < start:
                    continue
                elif mid <= end:
                    cnt += (mid - start) // gap + 1
                else:
                    cnt += (end - start) // gap + 1

            if cnt >= D:
                high = mid
            else:
                low = mid

        return high

sol = Solution()
print(sol.hidingDTR())