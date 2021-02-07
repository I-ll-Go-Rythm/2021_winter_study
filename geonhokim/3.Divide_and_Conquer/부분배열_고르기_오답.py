from typing import List

class Solution:
    def subArray(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]*arr[0]

        if len(arr) == 2:
            return max(arr[0]*arr[0], arr[1]*arr[1], sum(arr) * min(arr))

        maxSum = 0
        
        piver = len(arr) // 2

        for i in range(piver, len(arr)):
            sum_ = sum(arr[piver: i + 1]) * min(arr[piver: i + 1])
            print(arr[piver: i + 1])
            if maxSum < sum_:
                maxSum = sum_
        
        for i in range(piver - 1, -1, -1):
            sum_ = sum(arr[i:piver]) * min(arr[i:piver])
            print(arr[i:piver])
            if maxSum < sum_:
                maxSum = sum_

        start = piver
        end = piver + 1

        while start != 0 or end != len(arr) - 1:
            sum_ = sum(arr[start:end]) * min(arr[start:end])
            if maxSum < sum_:
                maxSum = sum_

            if arr[start - 1] > arr[end] or end == len(arr) - 1:
                start -= 1
            
            elif arr[start - 1] <= arr[end] or start == 0:
                end += 1
            


        return maxSum



sol = Solution()

n = int(input())

arr = list(map(int, input().split()))

print(sol.subArray(arr))