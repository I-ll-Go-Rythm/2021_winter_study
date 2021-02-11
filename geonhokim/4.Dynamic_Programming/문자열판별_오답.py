# 오답
# aaaaaaaaaa
# aaaa
# aaa
# 인경우 되지 않는다.

class Solution:
    def check(self):
        A = input()
        N = int(input())
        S = []

        for _ in range(N):
            S.append(input())
        
        dp = [0 for _ in range(len(A))] + [1]

        end = len(A)
        for start in range(len(A)-1, -1, -1): # A의 뒤부터 살펴보는데 test -> ntest -> ontest -> contest
            if (A[start:end] in S and dp[start + len(A[start:end])] == 1): # contest가 S리스트에 있고 start부터 그 길이만큼의 인덱스가 1이라면
                dp[start] = 1 
                # end = start
        print(dp)
        return int(dp[0] == 1)


sol = Solution()
print(sol.check())