# 오답
# 반례 6, 2  3, 4  4, 2

import sys

class Solution:
    def connectedComponent(self):
        N, M = map(int, sys.stdin.readline().split())
        if M == 0:
            return N
        arr = [[0] * (N + 1) for _ in range(N + 1)] 
        for _ in range(M):
            i, j = map(int, sys.stdin.readline().split())
            arr[i][j] = 1
            arr[j][i] = 1

        # for i in range(1, N + 1):
        #     for j in range(1, N + 1):
        #         print(arr[i][j], end='')
        #     print()
        
        visited = []
        cnt = 0
        for i in range(1, N + 1):
            if i not in visited:
                visited.append(i)
                cnt += 1 
            for j in range(i + 1, N + 1):
                if arr[i][j] == 1 and j not in visited:
                    visited.append(j)

        return cnt

sol = Solution()
print(sol.connectedComponent())
