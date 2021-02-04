import sys
import heapq
si = sys.stdin.readline

class Solution:
    def priorityQueue(self):
        cnt, n, pq, rooms = 1, int(si()), [], []
        for _ in range(n):
            [a, b] = [int(e) for e in si().split()]
            heapq.heappush(pq, (a, b))
    
        heapq.heappush(rooms, heapq.heappop(pq)[1])
        while pq:
            curr = heapq.heappop(pq)
            if curr[0] < rooms[0]:
                cnt += 1
            else:
                heapq.heappop(rooms)
            heapq.heappush(rooms, curr[1])
        
        return cnt

sol = Solution()


print(sol.priorityQueue())