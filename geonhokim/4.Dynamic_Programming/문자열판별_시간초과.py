# 백준 질문 게시판 반례
# 시간초과

class Solution:
    def check(self):
        A = input()
        N = int(input())
        S = []

        for _ in range(N):
            S.append(input())
        
        dp = [0 for _ in range(len(A))] + [1]

        oneIndex = [len(A)]
        copyIndex = [len(A)]
        for start in range(len(A)-1, -1, -1):
            for end in oneIndex:
                if (A[start:end] in S and dp[start + len(A[start:end])] == 1): 
                    dp[start] = 1 
                    copyIndex.append(start)
            
            oneIndex = copyIndex

        return int(dp[0] == 1)


sol = Solution() 
print(sol.check())