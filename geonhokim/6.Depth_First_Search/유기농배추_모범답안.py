from collections import deque
import sys

# 상 하 좌 우
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dfs(startV, field):
    queue = deque()
    queue.append(startV)

    while queue:
        x, y = queue.popleft()
        field[x][y] = 0

        for move in dirs:
            moved_x, moved_y = x + move[0], y + move[1]

            if 0 <= moved_x < M and 0 <= moved_y < N and field[moved_x][moved_y] == 1:
                queue.append((moved_x, moved_y))
                field[moved_x][moved_y] = 0
        
    return 1


T = int(input())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * N for _ in range(M)]
    cnt = 0

    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1

    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                cnt += dfs((i, j), field)

    print(cnt)