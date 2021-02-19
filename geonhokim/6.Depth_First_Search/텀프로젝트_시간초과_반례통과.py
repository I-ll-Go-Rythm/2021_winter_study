import sys

def dfs(startV: int):
    chk = []
    visited[startV] = True
    chk.append(startV)

    while True:
        startV = graph[startV]

        if startV in chk:
            end = chk.index(startV)
            cnt = len(chk[:end])
            return cnt
        
        if visited[startV] == True:
            cnt = len(chk)
            return cnt

        visited[startV] = True
        chk.append(startV)


T = int(input())
for _ in range(T):
    N = int(input())
    visited = [False for _ in range(N + 1)]

    graph = {}
    selects = [0]
    selects += list(map(int, sys.stdin.readline().split()))

    for i in range(1, N + 1):
        graph[i] = selects[i]
    
    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == False:
            cnt += dfs(i)
    
    print(cnt)