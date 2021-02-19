# graph를 따로 할당해줄 필요 없다.
# 이게 왜 시간초과지?

import sys

def dfs(startV: int):
    visited[startV] = True
    cntValue = 0
    cnt.append(startV)
    cntValue += 1

    while True:
        startV = selects[startV]

        if visited[startV] == True:
            if startV in cnt:
                return cnt.index(startV)
            return cntValue

        visited[startV] = True
        cnt.append(startV)
        cntValue += 1 # cnt Value로 바꿔주니까 통과 len()이 시간복잡도 많이 잡아먹어서 그런듯..
        

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