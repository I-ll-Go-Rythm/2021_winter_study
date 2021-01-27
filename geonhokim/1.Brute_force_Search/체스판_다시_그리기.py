import sys

class solution:
    def compare(self, board_line: str, num: int) -> int:
        A = 'BWBWBWBW'
        B = 'WBWBWBWB'
        cnt = 0

        if num%2 == 0:
            for i in range(8):
                if board_line[i] != A[i]:
                    cnt += 1
            return cnt

        else:
            for i in range(8):
                if board_line[i] != B[i]:
                    cnt += 1
            return cnt

        
    def myself(self, n: int, m: int) -> int:
        board = []

        min_redraw_cnt = sys.maxsize

        for _ in range(n):
            board.append(input())
        
        row = n - 8 + 1
        col = m - 8 + 1

        for i in range(row):
            for j in range(col):
                redraw_cnt = 0
                for k in range(0, 8):
                    redraw_cnt += self.compare(board[i+k], k)
                
                min_redraw_cnt = min(min_redraw_cnt, redraw_cnt)

                redraw_cnt = 0
                for k in range(0, 8):
                    redraw_cnt += self.compare(board[i+k], k + 1)
                
                min_redraw_cnt = min(min_redraw_cnt, redraw_cnt)

        return min_redraw_cnt
                

sol = solution()

n, m = map(int, input().split())

print(sol.myself(n, m))