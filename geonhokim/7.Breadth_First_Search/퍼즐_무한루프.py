import sys
from collections import deque
from typing import List

def swap(v: List[int], i: int, j: int):
    w = v[:]
    w[i], w[j] = w[j], w[i]
    
    return w


def bfs(puzzle: List[List[int]]) -> int:
    isVisit = [puzzle]
    q = deque([puzzle])

    depth = 0
 
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            if v == [1,2,3,4,5,6,7,8,0]:
                return depth

            idx = v.index(0)

            if idx % 3 == 1:
                for x in [-3, -1, +1, +3]: # 이거 아님
                    if 0 <= idx + x < 9:
                        w = swap(v, idx, idx + x)
                        if w not in isVisit:
                            q.append(w)
                            isVisit.append(w)
                
            elif idx % 3 == 0:
                for x in [-3, +1, +3]:
                    if 0 <= idx + x < 9:
                        w = swap(v, idx, idx + x)
                        if w not in isVisit:
                            q.append(w)
                            isVisit.append(w)

            else:
                for x in [-3, -1, +3]:
                    if 0 <= idx + x < 9:
                        w = swap(v, idx, idx + x)
                        if w not in isVisit:
                            q.append(w)
                            isVisit.append(w)                    
        
        depth += 1
    
    return -1


puzzle = []

for _ in range(3):
    puzzle.extend(list(map(int, sys.stdin.readline().split())))

print(bfs(puzzle))