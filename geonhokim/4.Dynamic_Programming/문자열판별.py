class Solution:
    def check(self):
        A = input()
        N = int(input())
        S = []

        for _ in range(N):
            S.append(input())
        
        dp = [0 for _ in range(len(A))] + [1]


        for end in range(len(A), 0, -1):
            for start in range(len(A) - 1, -1, -1):
                if (A[start:end] in S and dp[start + len(A[start:end])] == 1): 
                    dp[start] = 1 

        return int(dp[0] == 1)


sol = Solution() 
print(sol.check())