# g count를 구하는 방식
# 반례가 너무 많다.
# GGR
# RRG
# RRG

from collections import deque
import sys
sys.setrecursionlimit(10000)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = []
isG = [False]
def dfs(startV, color, visited):
    queue = deque()
    visited.append(startV)
    queue.append(startV)

    while queue:
        x, y = queue.popleft()
        if color == 'G':
            isG[0] = True
            img[x][y] = 'R'

        for move in dirs:
            moved_x, moved_y = x + move[0], y + move[1]

            if 0 <= moved_x < N and 0 <= moved_y < N and \
                img[moved_x][moved_y] == color and \
                    (moved_x, moved_y) not in visited:
                    dfs((moved_x, moved_y), color, visited)
    
    return isG[0]


N = int(input())
img = [[''] * N for _ in range(N)]

for i in range(N):
    rgb = list(input())
    
    for j in range(N):
        img[i][j] = rgb[j]
cnts = []
cnt = 0
gCnt = 0

for i in range(N):
    for j in range(N):
        if (i, j) not in visited:
            isG[0] = False
            isG[0] = dfs((i, j), img[i][j], visited)
            cnt += 1
            if isG[0]:
                gCnt += 1

print(cnt, cnt-gCnt)