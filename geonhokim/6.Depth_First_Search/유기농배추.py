import sys
sys.setrecursionlimit(10000)

class Solution:
    def __init__(self):
        self.graph = {}
        self.visited = []

    def dfs_recursive(self, startV):
        if startV not in self.visited:
            self.visited.append(startV)
        
            for w in self.graph[startV]:
                if w not in self.visited:
                    self.dfs_recursive(w)
            
            return True
        return False

    def organicCabbage(self):
        T = int(input())
        for _ in range(T):
            self.graph = {}
            self.visited = []
            M, N, K = map(int, sys.stdin.readline().split())
            field = [[0] * N for _ in range(M)]

            for _ in range(K):
                x, y = map(int, sys.stdin.readline().split())
                field[x][y] = 1
                self.graph[(x, y)] = []

            for i in range(M):
                for j in range(N):
                    if field[i][j] == 1:
                        if field[max(i-1, 0)][j] == 1:
                            if i != max(i-1, 0):
                                self.graph[(i, j)].append((max(i-1, 0), j))

                        if field[min(i+1, M-1)][j] == 1:
                            if i != min(i+1, M-1):
                                self.graph[(i, j)].append((min(i+1, M-1), j))

                        if field[i][max(j-1, 0)] == 1:
                            if j != max(j-1, 0):
                                self.graph[(i, j)].append((i, max(j-1, 0)))

                        if field[i][min(j+1, N-1)] == 1:
                            if j != min(j+1, N-1):
                                self.graph[(i, j)].append((i, min(j+1, N-1)))

            cnt = 0

            for loc in self.graph:
                if self.dfs_recursive(loc):
                    cnt += 1

            print(cnt)
        
        return


sol = Solution()
sol.organicCabbage()