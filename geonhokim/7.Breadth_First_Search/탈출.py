import sys
from collections import deque

def bfs(startV: int):
    isVisit[startV] = True
    q = deque()
    q.append(startV)

    depth = 0

    while q:
        if depth > T:
            return "ANG"

        for _ in range(len(q)):
            v = q.popleft()
            
            if v == G:
                return depth

            for button in ['A', 'B']:
                if button == 'A':
                    movedY = v + 1
                else:
                    if v == 0:
                        continue
                    if v * 2 > 99999:
                        break
                    x = list(str(v * 2))
                    x[0] = str(int(x[0]) - 1)

                    movedY, e = 0, 1
                    for i in range(len(x) - 1, -1, -1):
                        movedY += int(x[i]) * e
                        e *= 10

                if 0 <= movedY <= 99999:
                    if not isVisit[movedY]:
                        q.append(movedY)
                        isVisit[movedY] = True
        
        depth += 1
    
    return "ANG"

N, T, G = map(int, sys.stdin.readline().split())

isVisit = [False for _ in range(100000)]

print(bfs(N))