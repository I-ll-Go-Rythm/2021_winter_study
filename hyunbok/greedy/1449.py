N, L = map(int, input().split())
location = []
location = list(map(int, input().split()))
location.sort()

start = 0
ans = 0

for loc in location:
    if start<loc:
        start = loc+L-1
        ans +=1
print(ans)
