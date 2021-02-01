from itertools import combinations

n, s = map(int, input().split())
g = []
g = map(int, input().split())
graph = list(g)
ans = 0

for a in range(n):
    length = a+1
    k = list(combinations(graph, length))
    for _ in range(len(k)):
        if sum(k[_])==s:
            ans +=1
print(ans)


