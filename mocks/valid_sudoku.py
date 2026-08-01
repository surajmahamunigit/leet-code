# Algorithm:
# given 9*9  sudoku board, find if its valid
# use defaultdict to store each number in its  respective row, column and square
# if board[row][column] == "." -> skip
# we trace each number in sudoku board, example board[0][0]
# first we will check if exist in row[0], column[0], and square [(row//3, column//3)]
# -> if present return False, else add it to row[0], column[0], and square[(row//3, column//3)]
# repeat it till end of board. in end return True

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[int]]) -> bool:
        """Find the given 9*9 sudoku board is valid or not.

        Args:
            board: 9*9 sudoku board

        Returns:
            True if board is valid else False

        Time: O(1) - 9*9 = 81 checks
        Space: O(1) - 9*9 board
        """

        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):

                num = board[row][col]

                # "." check
                if num == ".":
                    continue

                # checks
                if num in rows[row] or num in columns[col] or num in squares[(row//3, col//3)]:
                    return False

                # else add it
                rows[row].add(num)
                columns[col].add(num)
                squares[(row//3, col//3)].add(num)

        return True
board1 =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
board2 =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
s = Solution()
assert s.isValidSudoku(board1) == True
assert s.isValidSudoku(board2) == False
print("passed")