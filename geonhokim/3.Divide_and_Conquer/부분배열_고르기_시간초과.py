# 시간초과
from typing import List

class Solution:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.maxSum = -1

    def subArray(self, leftStart: int, rightEnd: int) -> int:
        mid = (leftStart + rightEnd) // 2

        if rightEnd - leftStart == 1: # 길이가 1 or 2일 때,
            self.maxSum = max(self.maxSum, self.arr[leftStart] ** 2, self.arr[rightEnd] ** 2)
            return
        
        if rightEnd - leftStart == 0:
            self.maxSum = max(self.maxSum, self.arr[leftStart] ** 2)
            return

        self.subArray(leftStart, mid)
        self.subArray(mid + 1, rightEnd)

        left = mid
        right = mid
        
        while left != leftStart or right != rightEnd:
            if left != leftStart and (right == rightEnd or self.arr[left - 1] > self.arr[right + 1]):
                left -= 1

                self.maxSum = max(self.maxSum, sum(arr[left:right + 1]) * min(arr[left:right + 1]))
                continue

            if right != rightEnd and (left == leftStart or self.arr[left - 1] <= self.arr[right + 1]):
                right += 1

                self.maxSum = max(self.maxSum, sum(arr[left:right + 1]) * min(arr[left:right + 1]))
                continue

        return

        


n = int(input())

arr = list(map(int, input().split()))

sol = Solution(arr)


sol.subArray(0, n - 1)

print(sol.maxSum)