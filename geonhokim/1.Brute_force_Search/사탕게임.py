from typing import List

class solution:
    def __init__(self, n):
        self.max_line = 0
        self.n = n
    

    def width(self, XorI: int, candy_board):
        temp_max_line = 0

        for y in range(self.n - 1):
            if candy_board[XorI][y] == candy_board[XorI][y+1]:
                temp_max_line += 1

                if temp_max_line + 1 >= self.max_line:
                    self.max_line = temp_max_line + 1

            else:
                temp_max_line = 0


    def height(self, YorJ: int, candy_board):
        temp_max_line = 0

        for x in range(self.n - 1):
            if candy_board[x][YorJ] == candy_board[x+1][YorJ]:
                temp_max_line += 1

                if temp_max_line + 1 >= self.max_line:
                    self.max_line = temp_max_line + 1

            else:
                temp_max_line = 0     


    def brute_force(self, candy_board: List[List[str]]) -> int:
        for i in range(self.n):
            for j in range(self.n-1):
                candy_board[i][j], candy_board[i][j+1] = candy_board[i][j+1], candy_board[i][j]
                
                self.width(i, candy_board)

                for y in range(j, j + 1 + 1):
                    self.height(y, candy_board)

                candy_board[i][j], candy_board[i][j+1] = candy_board[i][j+1], candy_board[i][j]
                
        for i in range(self.n - 1):
            for j in range(self.n):
                candy_board[i][j], candy_board[i+1][j] = candy_board[i+1][j], candy_board[i][j]
                
                self.height(j, candy_board)

                for x in range(i, i + 1 + 1):
                    self.width(x, candy_board)


                candy_board[i][j], candy_board[i+1][j] = candy_board[i+1][j], candy_board[i][j]

        return self.max_line


n = int(input())

candy_board = []

for i in range(n):
    row_i = list(input())
    candy_board.append(row_i)

sol = solution(n)

print(sol.brute_force(candy_board))
