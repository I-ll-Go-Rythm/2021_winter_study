n = int(input())
dp = [0 for i in range(n + 1)]# [0,0,0,0,0,---,0] n+1개.
square = [i * i for i in range(1, 317)]#[1,4,9,16 --- <=100000]
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])#dp 핵심...헷갈린다 어케 짜지 이런걸
    dp[i] = min(s) + 1
print(dp[n])