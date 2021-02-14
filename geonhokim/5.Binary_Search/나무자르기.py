class Solution:
    def cutTree(self) -> int:
        N, M = map(int, input().split())
        tree = list(map(int, input().split()))

        maxHeight = max(tree)

        bot, top = 0, maxHeight

        while bot + 1 < top:
            mid = (top + bot)//2

            sum_ = 0
            for height in tree:
                if height - mid < 0:
                    continue
                sum_ += height - mid
            
            if sum_ < M:
                top = mid
            
            else:
                bot = mid

        return bot


sol = Solution()

print(sol.cutTree())