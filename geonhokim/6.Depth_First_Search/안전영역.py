from collections import deque
import sys

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()

def dfs(startV: int):
    x, y = startV
    chk[x][y] = 0
    q.append(startV)

    while q:
        x, y = q.pop()
        
        for move in dirs:
            moved_x, moved_y = x + move[0], y + move[1]

            if 0 <= moved_x < N and 0 <= moved_y < N:
                if chk[moved_x][moved_y] == 1:
                    q.append((moved_x, moved_y))
                    chk[moved_x][moved_y] = 0
    

N = int(input())
region = []

for _ in range(N):
    region.append(list(map(int, sys.stdin.readline().split())))

maxPptn = max(map(max, region))
max_cnt = 0
for pptn in range(0, maxPptn):
    chk = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if region[i][j] - pptn > 0:
                chk[i][j] = 1
            else:
                chk[i][j] = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if chk[i][j] == 1:
                dfs((i, j))
                cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)