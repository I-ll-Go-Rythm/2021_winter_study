N, K = map(int, input().split())
coins = []
coins = [input() for _ in range(N)]

coins.reverse()

ans = 0

for coin in coins:
    if K < int(coin): continue
    else:
        ans = ans + K//int(coin)
        K = K - int(coin)*(K//int(coin))
    if K == 0 : break

print(ans)


