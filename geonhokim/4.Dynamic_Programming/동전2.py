class Solution:
    def main(self, n: int, k: int) -> int:
        impossible = 10001
        coin = [0] + [impossible for _ in range(k)]

        for _ in range(n):
            value = int(input())

            for i in range(value, k + 1):
                if coin[i - value] == impossible:
                    continue

                coin[i] = min(coin[i], coin[i - value] + 1)

        if coin[-1] != impossible:
            return coin[-1]
        else:
            return -1


sol = Solution()

n, k = map(int, input().split())

print(sol.main(n, k))