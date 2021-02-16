import sys
N, C = map(int, (input().split()))
house = [int(sys.stdin.readline()) for _ in range(N)]

def router_counter(distance):
    count = 1
    cur_house = house[0] 
    for i in range(1, N): 
        if cur_house + distance <= house[i]: 
            count += 1
            cur_house = house[i] 
    return count

house = sorted(house) 
start, end = 1, house[-1] - house[0] 

while start <= end: 
    mid = (start+end) // 2
    
    if router_counter(mid) >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)