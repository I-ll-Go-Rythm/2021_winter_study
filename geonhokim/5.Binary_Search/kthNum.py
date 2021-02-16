class Soltuion:
    def Kth(self):
        N = int(input())
        K = int(input())

        low, high = 0, K + 1

        while low + 1 < high:
            mid = (low + high) // 2

            cnt = 0
            for i in range(1, N + 1):
                cnt += min(mid//i, N)

            if cnt < K:
                low = mid
            else:
                high = mid

        return high


sol = Soltuion()
print(sol.Kth())