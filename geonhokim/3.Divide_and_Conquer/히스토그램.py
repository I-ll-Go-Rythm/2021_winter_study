from typing import List

class Solution:
    def __init__(self, graph: List[int]):
        self.graph = graph
        
    def histogram(self, leftStart: int, rightEnd: int):
        if leftStart == rightEnd:
            return self.graph[leftStart]
        
        mid = (leftStart + rightEnd) // 2

        maxArea = max(self.histogram(leftStart, mid), self.histogram(mid + 1, rightEnd))
        
        left = mid
        right = mid

        length = 1
        min_ = self.graph[left]
        
        while left > leftStart or right < rightEnd:
            if left > leftStart and (right == rightEnd or self.graph[left - 1] > self.graph[right + 1]):
                left -= 1
                min_ = min(min_, self.graph[left])

            else:
                right += 1
                min_ = min(min_, self.graph[right])
            
            length += 1
            maxArea = max(maxArea, length * min_)

        return maxArea

n = int(input())

graph = []

for _ in range(n):
    graph.append(int(input()))

maxArea = -1

sol = Solution(graph)

print(sol.histogram(0, n - 1))