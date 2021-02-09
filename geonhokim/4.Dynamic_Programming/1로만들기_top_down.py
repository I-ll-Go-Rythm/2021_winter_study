from typing import List

class Solution:
    def __init__ (self, arr: List[int]):
        self.arr = arr

    def makeToOne(self, N: int):
        if N == 1:
            return 0

        for i in range(2, N + 1):
            result1 = self.arr[i-1] + 1
            result2 = 10000000
            result3 = 10000000

            if i % 2 == 0:
                result2 = self.arr[i//2] + 1
            if i % 3 == 0:
                result3 = self.arr[i//3] + 1

            self.arr[i] = min(result1, result2, result3)
        
        return self.arr[i]

N = int(input())

arr = [0] * (N + 1)

sol = Solution(arr)

print(sol.makeToOne(N))