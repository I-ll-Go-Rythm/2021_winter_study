import sys

def dfs(startV: int):
    stack = [startV]
    cnt = 0
    while stack:
        v = stack.pop()
        cnt += 1
        if cnt > M : # 숫자가 들어가있는 graph 길이로 하면 더 정확?
            return -1
        for w in graph[v]:
            stack.append(w)

    return cnt - 1
    

N, M, P = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(M + 1)]

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if graph[b] == []:
        graph[b].append(a)


cnt = dfs(P)

print(cnt)