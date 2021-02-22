import sys
from collections import deque

def bfs(curS: int):
    visited[curS] = True
    q = deque()
    q.append(curS)
    depth = 0

    while q:
        for _ in range(len(q)):
            v = q.popleft()

            if v == targetG:
                return depth

            for move in [U, -D]:
                movedS = v + move

                if 0 < movedS <= maxF:
                    if visited[movedS] == False:
                        q.append(movedS)
                        visited[movedS] = True

        depth += 1
    return "use the stairs"


maxF, curS, targetG, U, D = map(int, sys.stdin.readline().split())

visited = [False for _ in range(maxF + 1)]

print(bfs(curS))