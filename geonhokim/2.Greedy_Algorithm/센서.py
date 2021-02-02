class Solution:
    def myself(self, N: int, K: int) -> int:
        if N == 1 or N <= K:
            return 0

        sensors = list(map(int, input().split()))
        sensors.sort()

        distance_between_snesors = []

        min_length = 0

        for i in range(1, len(sensors)):
            distance = sensors[i] - sensors[i - 1]
            distance_between_snesors.append(distance)
        
        for number_of_center in range(N - 1, 0, -1):
            min_length += min(distance_between_snesors)
            distance_between_snesors.remove(min(distance_between_snesors))
            print(f'집중국 개수: {number_of_center} \n 최소 길이: {min_length}')
            if number_of_center == K:
                return min_length

sol = Solution()

N = int(input())
K = int(input())

print(sol.myself(N, K))