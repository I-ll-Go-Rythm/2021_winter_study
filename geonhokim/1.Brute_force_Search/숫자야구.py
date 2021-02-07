from itertools import permutations

class solution:
    def permutation_(self, n: int) -> int:
        num = list(permutations([1,2,3,4,5,6,7,8,9], 3))

        for _ in range(n):
            test, s, b = map(int, input().split())
            test = list(str(test))
            remove_cnt = 0

            for i in range(len(num)):
                i -= remove_cnt
                strk_cnt = 0
                ball_cnt = 0

                for j in range(3):
                    if int(test[j]) in num[i]:
                        if j == num[i].index(int(test[j])):
                            strk_cnt += 1

                        else:
                            ball_cnt += 1

                if strk_cnt != s or ball_cnt != b:
                    num.remove(num[i])
                    remove_cnt += 1
        
        return len(num)

sol = solution()

n = int(input())

print(sol.permutation_(n))

