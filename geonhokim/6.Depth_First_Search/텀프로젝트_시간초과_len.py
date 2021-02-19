# graph를 따로 할당해줄 필요 없다.
# 이게 왜 시간초과지?

import sys

def dfs(startV: int):
    visited[startV] = True
    cnt.append(startV)

    while True:
        startV = selects[startV]

        if visited[startV] == True:
            if startV in cnt:
                return cnt.index(startV)
            return len(cnt)

        visited[startV] = True
        cnt.append(startV)

for _ in range(int(input())):
    N = int(input())
    visited = [False] * (N + 1)
    selects = [0] + list(map(int, sys.stdin.readline().split()))

    ans = 0
    for i in range(1, N + 1):
        if visited[i] == False:
            cnt = []
            ans += dfs(i)
    
    print(ans)