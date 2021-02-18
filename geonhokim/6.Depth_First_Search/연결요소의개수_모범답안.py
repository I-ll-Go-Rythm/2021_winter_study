# https://velog.io/@devjuun_s/%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98-%EB%B0%B1%EC%A4%80-11724%EB%B2%88python

import sys
sys.setrecursionlimit(10000)

def dfs(v: int):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)

N, M = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1, N+1):
    if not visited[j]:
        dfs(j)
        cnt += 1

print(cnt)