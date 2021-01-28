from itertools import combinations

class solution:
    def myself(self, N:int, S:int) -> int:
        
        sequence = list(map(int, input().split()))

        cnt = 0

        for i in range(1, len(sequence) + 1):
            for part in list(combinations(sequence, i)):
                if sum(part) == S:
                    cnt += 1
            

        return cnt

sol = solution()

N, S = map(int, input().split())

print(sol.myself(N, S))