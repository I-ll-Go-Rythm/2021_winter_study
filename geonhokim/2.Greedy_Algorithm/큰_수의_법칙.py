import time

startTime = time.time()

N, M, K = map(int, input().split())

NList = list(map(int, input().split()))

sum = 0
cnt = 0

NList.sort()

first = NList[N - 1]
second = NList[N - 2]

for _ in range(M):
    if cnt == K:
        cnt = 0
        sum += second
        continue

    sum += first
    cnt += 1


print(sum)

endTime = time.time()

print(endTime - startTime)