from collections import deque
import sys

def bfs(startX: int, startY: int):
    visited = [(startX, startY)]
    q = deque()
    q.append((startX, startY))
    depth = 0

    while q:
        for _ in range(len(q)):
            vX, vY = q.popleft()

            for moveX in [-2, +2]:
                for moveY in [-1, +1]:
                    movedX = vX + moveX
                    movedY = vY + moveY
                    if 0 <= movedX < I and 0 <= movedY < I:
                        if (movedX, movedY) not in visited:
                            q.append((movedX, movedY))
                            visited.append((movedX, movedY))

            for moveX in [-1, +1]:
                for moveY in [-2, +2]:
                    movedX = vX + moveX
                    movedY = vY + moveY
                    if 0 <= movedX < I and 0 <= movedY < I:
                        if (movedX, movedY) not in visited:
                            q.append((movedX, movedY))
                            visited.append((movedX, movedY))

        depth += 1
        if (targetX, targetY) in visited:
            return depth


T = int(input())

for _ in range(T):
    I = int(input())
    
    startX, startY = map(int, sys.stdin.readline().split())
    targetX, targetY = map(int, sys.stdin.readline().split())

    if startX == targetX and startY and targetY:
        print(0)
    else:
        print(bfs(startX, startY))