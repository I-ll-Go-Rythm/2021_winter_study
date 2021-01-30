class Solution:
    def myself(self, L: int, P: int, V: int, i: int) -> str:
        result = (V//P)*L + min((V%P), L)
        answer = f"Case {i}: {result}"
        return answer


sol = Solution()

i = 1
while True:
    L, P, V = list(map(int, input().split()))
    if L == 0 and P == 0 and V == 0:
        break

    print(sol.myself(L, P, V, i))
    i += 1