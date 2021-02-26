import sys

cnt = 0

def dfs(idx, sum, N, S, seq):
    if idx >= N:
        return
    
    if sum + seq[idx] == S:
        cnt += 1
    
    dfs(idx+1, sum, N, S, seq)
    dfs(idx+1, sum + seq[idx], N, S, seq)


N, S = map(int, sys.stdin.readline().split())

seq = list(map(int, sys.stdin.readline().split()))

dfs(0, 0, N, S, seq)