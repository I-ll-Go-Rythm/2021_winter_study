class Solution:
    def myself(self, N: int):
        reserv_list = []
        stack = []

        cnt = 0

        for _ in range(N):
            start, end = map(int, input().split())

            reserv_list.append([start, end])
        
        # reserv_list.sort(key=lambda x: [x[1], x[0]])
        reserv_list.sort(key=lambda x: x[1])
        
        # for i in range(len(reserv_list)):
        #     if not stack:
        #         stack.append(reserv_list[i])
        #         continue

        #     if stack[-1][1] <= reserv_list[i][0]:
        #         stack.append(reserv_list[i])

        # return len(stack)
        
        return reserv_list

sol = Solution()

N = int(input())

print(sol.myself(N))