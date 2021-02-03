class Solution:
    def myself(self, L: int, N: int, rf: int, rb: int) -> int:
        tastiness = 0
        restStops = []

        for _ in range(N):
            xi, ci = map(int, input().split())
            restStops.append((xi, ci))

        restStops.sort(reverse=True, key=lambda x: (x[1], x[0]))
        
        start = 0

        for i in range(len(restStops)):
            if restStops[i][0] > start:
                tastiness += ((restStops[i][0] - start) * (rf - rb)) * restStops[i][1]
                start = restStops[i][0]

        return tastiness



sol = Solution()

L, N, rf, rb = map(int, input().split())

print(sol.myself(L, N, rf, rb))