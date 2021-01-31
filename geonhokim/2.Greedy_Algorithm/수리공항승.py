from typing import List

class Solution:
    def myself(self, L: int, leak_list: List[int]) -> int:
        cnt = 1

        leak_list.sort()

        i = 0
        j = 1
        while True:
            if i == len(leak_list) - 1 or i + j > len(leak_list) - 1:
                break
            
            if leak_list[i] - 0.5 + L >= leak_list[i + j] + 0.5:
                j += 1
            
            else:
                i, j = i + j, 1
                cnt += 1
                

        return cnt

sol = Solution()

N, L = map(int, input().split())

leak_list = list(map(int, input().split()))
print(sol.myself(L, leak_list))
