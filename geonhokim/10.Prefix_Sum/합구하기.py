import sys

N = int(input())

numList = list(map(int, sys.stdin.readline().split()))
pSum = [0 for _ in range(N + 1)]

for x in range(N):
    pSum[x + 1] = pSum[x] + numList[x]

M = int(input())

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    print(pSum[j] - pSum[i - 1])