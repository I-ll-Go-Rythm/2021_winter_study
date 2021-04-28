import time

startTime = time.time()

N, M, K = map(int, input().split())

NList = list(map(int, input().split()))

NList.sort()

first = NList[N - 1]
second = NList[N - 2]

# div = (M // (K + 1)) * (K * first + second)
# mod = (M % (K + 1)) * first

# print(div + mod)

count = (M // (K + 1)) * K
count += (M % (K + 1))

sum = 0
sum += count * first
sum += (M - count) * second

print(sum)

endTime = time.time()

print("time: ", endTime - startTime)