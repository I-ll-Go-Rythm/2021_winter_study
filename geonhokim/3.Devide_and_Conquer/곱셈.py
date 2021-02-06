class Solution:
    def mul(self, A: int, B: int, C: int) -> int:
        if B == 1:
            # if D == 1:
            return A % C
            # else:
            #     return C - A
        
        if B % 2 == 0:
            R1 = self.mul(A, B//2, C)
            
            return ((R1 % C) * (R1 % C)) % C
        else:
            R1 = self.mul(A, B//2, C)

            return ((R1 % C) * ((R1 * A) % C)) % C


sol = Solution()

A, B, C = map(int, input().split())

# if A >= C:
#     D = 1
# else:
#     D = 3

print(sol.mul(A, B, C))