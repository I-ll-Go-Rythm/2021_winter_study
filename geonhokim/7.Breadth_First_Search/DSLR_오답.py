#반례
# 1
# 2 1
# None/ ans = S
import sys
from collections import deque

def bfs(startV):
    isVisit[int(startV)] = True
    q = deque([(startV, '')])


    while q:
        for _ in range(len(q)):

            v, result = q.popleft()
            if v == B:
                return result
            
            for cmd in ['D', 'S', 'L', 'R']:
                if cmd == 'D':
                    w = (int(v) * 2) % 10000

                if cmd == 'S':
                    w = int(v) - 1
                    if w == -1:
                        w = 9999

                if cmd == 'L':
                    X = list('0' * (4 - len(v)) + v)
                    
                    w = X[1] + X[2] + X[3] + X[0]

                if cmd == 'R':
                    X = list('0' * (4 - len(v)) + v)
                    # X = list(v)
                    w = X[3] + X[0] + X[1] + X[2]

                if not isVisit[int(w)]:
                    q.append((str(w), result + cmd))
                    isVisit[int(w)] = True



for _ in range(int(input())):
    A, B = sys.stdin.readline().split()
    A = '0' * (4 - len(A)) + A
    B = '0' * (4 - len(B)) + B
    print(B)
    isVisit = [False for _ in range(10000)]

    print(bfs(A))