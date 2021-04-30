N, M = map(int, input().split())

max_ = 0

for _ in range(N):
    cards = list(map(int, input().split()))
    
    minCard = min(cards)
    max_ = max(minCard, max_)

print(max_)