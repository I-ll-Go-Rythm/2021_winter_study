# 왜 visited에다 담아서 체크하는 방식은 안되는거야
# chk 2차원 배열은 인덱스 탐색으로 시간복잡도 O(1)
# 그러나 visited에다가 N*N을 다담아서 if (moved_x, moved_y) in visited하면
# 시간복잡도 O(n^2) 이라서 그런가 
import sys

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(startV):
    stack = []
    stack.append(startV)

    while stack:
        x, y = stack.pop()

        for move in dirs:
            moved_x, moved_y = x + move[0], y + move[1]

            if 0 <= moved_x < N and 0 <= moved_y < N and \
                chk[moved_x][moved_y] == 0 and \
                    img[moved_x][moved_y] == img[x][y]:
                    chk[moved_x][moved_y] = 1
                    stack.append((moved_x, moved_y))
    
N = int(input())
img = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
chk = [[0]*N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if chk[i][j] == 0:
            chk[i][j] = 1
            dfs((i, j))
            cnt += 1

print(cnt, end=' ')

cnt = 0

for i in range(N):
    for j in range(N):
        if img[i][j] == 'G':
            img[i][j] = 'R'

chk = [[0]*N for _ in range(N)]


for i in range(N):
    for j in range(N):
        if chk[i][j] == 0:
            chk[i][j] = 1
            dfs((i, j))
            cnt += 1

print(cnt, end=' ')