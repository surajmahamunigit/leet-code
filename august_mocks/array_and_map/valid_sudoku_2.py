# 9.29
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """Find out if given board is valid or not.

        Args:
            board: given 9*9 sudoku board

        Returns:
            True if board is valid, else False

        Time: O(1)
        Space: O(1)
        """
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                sq_index = (row//3, col//3)
                char = board[row][col]

                if char == ".":
                    continue

                if char in rows[row] or char in columns[col] or char in squares[sq_index]:
                    return False

                else:
                    rows[row].add(char)
                    columns[col].add(char)
                    squares[sq_index].add(char)

        return True

s = Solution()
valid_board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]  # -> True

invalid_board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],   # <-- duplicate 8 in column 0
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]  # -> False

box_only_duplicate = [["." for _ in range(9)] for _ in range(9)]
box_only_duplicate[0][0] = "5"
box_only_duplicate[2][1] = "5"   # same 3x3 box, different row and column

assert s.isValidSudoku(valid_board) == True
assert s.isValidSudoku(invalid_board) == False
assert s.isValidSudoku(box_only_duplicate) == False
print("passed")


# 9.37 -> 8 minutes to finish