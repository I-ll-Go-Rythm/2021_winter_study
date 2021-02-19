from typing import List
import sys
sys.setrecursionlimit(10000)

class Solution:
    def __init__(self, N: int, M: int):
        self.N = N
        self.M = M
        self.adj = [[] * (N + 1) for _ in range(N + 1)]
        self.visited = []

    def dfs_recursive(self, startV):
        if startV not in self.visited:
            self.visited.append(startV)

            for w in self.adj[startV]:
                if w not in self.visited:
                    self.dfs_recursive(w)
            
            return True
        return False

    def connectedComponent(self):
        for _ in range(self.M):
            u, v = map(int, sys.stdin.readline().split())
            self.adj[u].append(v)
            self.adj[v].append(u)

        cnt = 0

        for i in range(1, self.N + 1):
            isNew = self.dfs_recursive(i)

            if isNew:
                cnt += 1

        return cnt

N, M = map(int, input().split())
sol = Solution(N, M)
print(sol.connectedComponent())