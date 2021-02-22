import sys
from collections import deque

def bfs(startV: int):
    isVisit[startV] = True
    q = deque([(startV, '')])

    depth = 0
    while q:
        for _ in range(len(q)):

            v, result = q.popleft()
            if v == B:
                return result
            
            for cmd in ['D', 'S', 'L', 'R']:
                if cmd == 'D':
                    w = (v * 2) % 10000

                if cmd == 'S':
                    w = (v + 9999) % 10000

                if cmd == 'L':
                    X = list((str(v)))
                    if len(X) < 4:
                        a = ['0', '0', '0', '0']
                        a[-len(X):] = X
                        X = a
                    w = int(''.join(X[1:] + X[:1]))

                if cmd == 'R':
                    X = list((str(v)))
                    if len(X) < 4:
                        a = ['0', '0', '0', '0']
                        a[-len(X):] = X
                        X = a
                    w = int(''.join(X[-1:] + X[:-1]))
                
                if not isVisit[w]:
                    q.append((w, result + cmd))
                    isVisit[w] = True

        depth += 1


T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    isVisit = [False for _ in range(10000)]
    print(bfs(A))