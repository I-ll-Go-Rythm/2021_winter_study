import sys
from collections import deque

def dfs(startV: int):
    visited = []
    stack = [startV]
    while stack:
        v = stack.pop()

        if v not in visited:
            visited.append(v)

            graph[v].sort(reverse=True)
            for w in graph[v]:
                stack.append(w)
    
    for v in visited:
        print(v, end=' ')
    print()

    return

def bfs(startV: int):
    visited = [startV]
    q = deque()
    q.append(startV)

    while q:
        v = q.popleft()

        graph[v].sort()
        for w in graph[v]:
            if w not in visited:
                q.append(w)
                visited.append(w)


    for v in visited:
        print(v, end=' ')
    print()
    return


N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    startV, endV = map(int, sys.stdin.readline().split())
    graph[startV].append(endV)
    graph[endV].append(startV)

dfs(V)
bfs(V)