from typing import List
import sys

class solution:
    def two_pointer(self, heights: List[int]) -> List[int]:
        heights.sort()

        sumAll = sum(heights)
        left, right = 0, len(heights) - 1

        while left < right:
            a = sumAll - heights[left] - heights[right]
            if a > 100:
                left += 1

            elif a < 100:
                right -= 1

            else:
                for i in range(len(heights)):
                    if i != left and i != right:
                        print(heights[i])

                break
                     
                 

            
sol = solution()

heights = []

for _ in range(9):
    temp = int(sys.stdin.readline())
    heights.append(temp)

sol.two_pointer(heights)
