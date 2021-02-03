import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
        
class Solution:
    # 아이디어 보고 더럽게 푼거
    def fillBox(self, L: int, W: int, H: int, N: int) -> int:
        cubes = []

        for _ in range(N):
            square, num = map(int, input().split())
            cubes.append([2 ** square, num])
        
        cubes.sort(key = lambda x : (x[0]))

        before = 0
        cnt = 0

        for i in range(N - 1, -1, -1):
            cube_size = cubes[i][0]
            x, y, z = L // cube_size, W // cube_size, H // cube_size

            if x and y and z:
                sum = x * y * z

                if N == 1 and x * y * z != L * W * H:
                    return -1

                if before:
                    sum = sum - ((cubes[i + 1][0] // cube_size) ** 3) * before

                    if sum > cubes[i][1]:
                        if cubes[i][0] == 1:
                            return -1

                        sum = cubes[i][1]
                    
                    before = before * ((cubes[i + 1][0] // cube_size) ** 3) + sum
                    
                else:
                    if sum > cubes[i][1]:
                        if cubes[i][0] == 1:
                            return -1

                        sum = cubes[i][1]
            
                    before = before + sum
            
                cnt += sum
        
        if cnt == 0 or (W % cube_size) or (L % cube_size) or (H % cube_size):
            return -1

        return cnt

    # 블로그 참조, 비트연산
    # 대박...
    def BitwiseOperator(self, L: int, W: int, H: int, n: int):
        cubes = [0] * 21
        for _ in range(n):
            a, b = map(int, input().rstrip().split(" "))
            cubes[a] += b
        
        total = 0
        count = 0
        
        for i in range(19, -1, -1):
            total <<= 3 # 8x8x8은 4x4x4의 8배, 4x4x4는 2x2x2의 8배...
            t = min(cubes[i], (L >> i) * (W  >> i) * (H  >> i) - total) 
            total += t
            count += t
            
        if(total == L * W * H ):
            print(count)
        
        else:
            print(-1)



sol = Solution()


length, width, height = map(int, input().rstrip().split(" "))
n = int(input().rstrip())

print(sol.fillBox(length, width, height, n))

sol.BitwiseOperator(length, width, height, n)