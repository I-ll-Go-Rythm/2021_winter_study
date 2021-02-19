import sys

def dfs(startV: int, endV: int):
    visited = []
    stack = []
    stack.append(startV)
    cnt = 0
    while stack:
        v = stack.pop()
        if v == endV and cnt != 0:
            return True
        cnt += 1
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    
    return False


N = int(input())
routes = [[0] for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    routes[i].extend(list(map(int, sys.stdin.readline().split())))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if routes[i][j] == 1:
            graph[i].append(j)

answer = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dfs(i, j):
            answer[i][j] = 1
        else:
            answer[i][j] = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(answer[i][j], end =' ')
    print()
