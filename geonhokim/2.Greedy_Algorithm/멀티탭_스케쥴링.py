from collections import deque

class Solution:
    def myself(self, n: int, k: int) -> int:
        scheduling = deque(map(int, input().split()))
        hole = []
        cnt = 0

        # j = 0
        # while j < 10:
        #     j = j+1

        while scheduling:
            if scheduling[0] in hole:
                scheduling.popleft()
                continue
            
            if len(hole) < n:
                hole.append(scheduling.popleft())
                continue

            if scheduling[0] not in hole:
                next = scheduling.popleft()
                maxIndex = -1

                for i in range(len(hole)):
                    if hole[i] in scheduling:
                        maxIndex = max(maxIndex, scheduling.index(hole[i]))

                    else:
                        hole[i] = next
                        cnt += 1
                        break
                
                if next not in hole:
                    hole[hole.index(scheduling[maxIndex])] = next
                    cnt += 1

        return cnt


sol = Solution()

n, k = map(int, input().split())

print(sol.myself(n, k))