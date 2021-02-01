import sys
from itertools import permutations

n = int(input())
num = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(n):
    g, s, b = map(int, input().split())
    g = list(str(g))
    remove_temp = 0

    for i in range(len(num)):
        s_temp = b_temp = 0
        i -= remove_temp

        for j in range(3):
            g[j] = int(g[j])
            if g[j] in num[i]:
                if j == num[i].index(g[j]):
                    s_temp += 1
                else:
                    b_temp += 1

        if s_temp != s or b_temp != b:
            num.remove(num[i])
            remove_temp+=1
print(len(num))
