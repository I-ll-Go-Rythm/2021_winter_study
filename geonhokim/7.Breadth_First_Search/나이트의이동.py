from collections import deque
import sys

def bfs(startX: int, startY: int):
    isVisit[startX][startY] = True
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
                        if isVisit[movedX][movedY] == False:
                            q.append((movedX, movedY))
                            isVisit[movedX][movedY] = True


            for moveX in [-1, +1]:
                for moveY in [-2, +2]:
                    movedX = vX + moveX
                    movedY = vY + moveY
                    if 0 <= movedX < I and 0 <= movedY < I:
                        if isVisit[movedX][movedY] == False:
                            q.append((movedX, movedY))
                            isVisit[movedX][movedY] = True

        depth += 1
        if isVisit[targetX][targetY]:
            return depth


T = int(input())

for _ in range(T):
    I = int(input())
    isVisit = [[False for _ in range(I)] for _ in range(I)]

    startX, startY = map(int, sys.stdin.readline().split())
    targetX, targetY = map(int, sys.stdin.readline().split())

    if startX == targetX and startY == targetY:
        print(0)
    else:
        print(bfs(startX, startY))