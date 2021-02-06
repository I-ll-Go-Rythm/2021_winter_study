import heapq
import sys

N = int(input())
G = []
h = []
for i in range(N):
    G.append(list(map(int, input().split())))

G = sorted(G, key = lambda x : x[0])

for i in range(N):
    if len(h) != 0 and h[0] <=G[i][0]:
        heapq.heappop(h)
    heapq.heappush(h, G[i][1])

print(len(h))
