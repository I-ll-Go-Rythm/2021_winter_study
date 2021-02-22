import sys
from collections import deque

def bfs(startV: int):
    visited[startV] = True
    q = deque()
    q.append(startV)

    depth = 0

    while q:
        for _ in range(len(q)):
            v = q.popleft()
            if v == K:
                return depth
            
            for move in [-1, +1, 'double']:
                if move == 'double':
                    movedX = v * 2
                else:
                    movedX = v + move

                if 0 <= movedX <= N + K * 2:
                    if not visited[movedX]:
                        q.append(movedX)
                        visited[movedX] = True
        
        depth += 1

N, K = map(int, sys.stdin.readline().split())

visited = [False for _ in range(N + K * 2 + 1)] # N을 안더해주면 100 0 입력했을 때 에러

print(bfs(N))