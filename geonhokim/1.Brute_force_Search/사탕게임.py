from typing import List

class solution:
    def brute_force(self, candy_board: List[List[str]]) -> int:
        max_line = 0
        for i in range(n):
            for j in range(n-1):
                copy_board = candy_board
                
                temp = ''
                temp = copy_board[i][j]
                copy_board[i][j] = copy_board[i][j+1]
                copy_board[i][j+1] = temp
                
                temp_max_line = 0

                for y in range(n - 1):
                    if copy_board[i][y] == copy_board[i][y+1]:
                        temp_max_line += 1

                        if temp_max_line > max_line:
                            max_line = temp_max_line

                    else:
                        temp_max_line = 0

                for x in range(n - 1):
                    for y in range(j, j + 1 + 1):
                        if copy_board[x][y] == copy_board[x+1][y]:
                            temp_max_line += 1

                            if temp_max_line > max_line:
                                max_line = temp_max_line

                        else:
                            temp_max_line = 0

                
        for i in range(n - 1):
            for j in range(n):
                copy_board = candy_board
                
                temp = ''
                temp = copy_board[i][j]
                copy_board[i+1][j] = copy_board[i][j]
                copy_board[i+1][j] = temp
                
                temp_max_line = 0

                for x in range(n - 1):
                    if copy_board[x][j] == copy_board[x+1][j]:
                        temp_max_line += 1

                        if temp_max_line > max_line:
                            max_line = temp_max_line

                    else:
                        temp_max_line = 0

                for x in range(i, i + 1 + 1):
                    for y in range(n - 1):
                        if copy_board[x][y] == copy_board[x][y+1]:
                            temp_max_line += 1

                            if temp_max_line > max_line:
                                max_line = temp_max_line

                        else:
                            temp_max_line = 0

        return max_line

sol = solution()

n = int(input())

candy_board = []

for i in range(n):
    row_i = list(input())
    candy_board.append(row_i)


print(sol.brute_force(candy_board))




