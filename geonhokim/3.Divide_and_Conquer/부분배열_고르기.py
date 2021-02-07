# 시간초과
from typing import List

class Solution:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.maxSum = -1

    def subArray(self, leftStart: int, rightEnd: int) -> int:

        if rightEnd - leftStart == 0:
            # return self.arr[leftStart] ** 2 여기가 잘못됨 만약에 n - 1 값을 줬을 때, -1을 반환하게 한다.
            self.maxSum = self.arr[leftStart] ** 2
            return self.maxSum
        
        mid = (leftStart + rightEnd) // 2

        self.maxSum = max(self.subArray(leftStart, mid), self.subArray(mid + 1, rightEnd))

        left = mid
        right = mid + 1
        
        sum_ = self.arr[left] + self.arr[right]
        min_ = min(self.arr[left], self.arr[right])
        self.maxSum = max(self.maxSum, sum_ * min_)

        while left > leftStart or right < rightEnd:
            if right < rightEnd and (left == leftStart or self.arr[left - 1] < self.arr[right + 1]):
                right += 1

                sum_ += self.arr[right]
                min_ = min(self.arr[right], min_)
            else:
                left -= 1

                sum_ += self.arr[left]
                min_ = min(self.arr[left], min_)
            self.maxSum = max(self.maxSum, sum_ * min_)

        return self.maxSum

        


n = int(input())

arr = list(map(int, input().split()))

sol = Solution(arr)


sol.subArray(0, n - 1)

print(sol.maxSum)