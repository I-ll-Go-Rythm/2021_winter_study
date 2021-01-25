import sys
from typing import List

class solution:
    def triangle(self, n: int) -> int:
        return n * (n + 1) // 2

    def brute_force(self, num: int):
        for i in range(1, 45):
            for j in range(1, 45):
                for k in range(1, 45):
                    if i != 0 and j != 0 and k != 0 and self.triangle(i) + self.triangle(j) + self.triangle(k) == num:
                        return 1

        return 0


sol = solution()

k = int(input())
num_list = []

for _ in range(k):
    temp = int(sys.stdin.readline())
    num_list.append(temp)

for num in num_list:
    print(sol.brute_force(num))