import sys
from collections import deque

def bfs(startV):
    isVisit[int(startV)] = True
    q = deque([(startV, '')])


    while q:
        for _ in range(len(q)):

            cur, result = q.popleft()
            if cur == B:
                return result
            
            for cmd in ['D', 'S', 'L', 'R']:
                if cmd == 'D':
                    w = str((int(cur) * 2) % 10000)

                if cmd == 'S':
                    if w == '0000':
                        w = '9999'
                    else:
                        w = str(int(cur) - 1)
                if cmd == 'L':                    
                    w = cur[1] + cur[2] + cur[3] + cur[0]

                if cmd == 'R':
                    w = cur[3] + cur[0] + cur[1] + cur[2]

                w = '0' * (4 - len(w)) + w
                if not isVisit[int(w)]:
                    q.append((str(w), result + cmd))
                    isVisit[int(w)] = True



for _ in range(int(input())):
    A, B = sys.stdin.readline().split()
    A = '0' * (4 - len(A)) + A
    B = '0' * (4 - len(B)) + B

    isVisit = [False for _ in range(10000)]

    print(bfs(A))