# algorithm
# given board is 9*9, each row has 9 characters, every column has 9 characters and every 3*3 square has 9 characters
# we will use defaultdicts to store each row, column and square named rows, columns, squares
# for each character will will check if its equal to ".", if yes, skip it
# if not, check each character at board[row][column]  is in respective dicts or not like rows[row], columns[column], squares[(row//3,column//3)
# if present return False, else add to respective row, column and square dict.

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """Find out if given 9*9 sudoku board is valid or not.

        Args:
            board: 9*9 sudoku board containing "." and numbers

        Returns:
            True if board is valid, else False

        Time: O(1) - 9*9 = 81 possible numbers
        Space: O(1) - rows, columns, squares would hold max 81 numbers
        """

        rows = defaultdict(set)
        columns = defaultdict(set)
        squares  = defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num == ".":
                    continue

                if num in rows[row] or num in columns[col] or num in squares[(row//3,col//3)]:
                    return False

                rows[row].add(num)
                columns[col].add(num)
                squares[(row//3,col//3)].add(num)

        return True

valid_board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]

invalid_board = [
  ["8","3",".",".","7",".",".",".","."],   # <-- two 8s in the leftmost column (row 0 and row 3)
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]

s = Solution()
assert s.isValidSudoku(valid_board) == True
assert s.isValidSudoku(invalid_board) == False
print("passed")

