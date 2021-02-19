from collections import deque
import sys
sys.setrecursionlimit(100000)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
a = [0]
def dfs(startV: int):
    queue = deque()
    queue.append(startV)
    
    while queue:
        x, y = queue.popleft()
        graphPaper[x][y] = 0
        a[0] += 1

        for move in dirs:
            moved_x, moved_y = x + move[0], y + move[1]

            if 0 <= moved_x < N and 0 <= moved_y < M and graphPaper[moved_x][moved_y] == 1:
                dfs((moved_x, moved_y))
    
    return a[0]
        

M, N, K = map(int, sys.stdin.readline().split())
graphPaper = [[1] * M for _ in range(N)]

for _ in range(K):
    xs, ys, xe, ye = map(int, sys.stdin.readline().split())
    for i in range(xs, xe):
        for j in range(ys, ye):
            graphPaper[i][j] = 0

cnt = 0
areas = []

for i in range(N):
    for j in range(M):
        if graphPaper[i][j] == 1:
            a[0] = 0
            areas.append(dfs((i, j)))
            cnt += 1

print(cnt)
for area in sorted(areas):
    print(area, end=' ')