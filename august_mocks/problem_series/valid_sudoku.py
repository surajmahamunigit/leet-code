# 9.25
# given 9*9 sudoku board and asked to find out if board is valid or not
# start with board[0][0] and check in row number 0 set , column number 0 and square number 0,0
# if "." skip, if duplicate found return False
# arra and hash pattern

from collections import defaultdict

class Solution:
    def validSudoku(self, board: list[list[str]]) -> bool:
        """Find out if given board is valid or not.

        Args:
            board: 9*9 sudoku board

        Returns:
            True if board is valid, else False

        Time: O(1) - 9*9 board
        Space: O(1)
        """

        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                char = board[row][col]

                if char == ".":
                    continue

                if char in rows[row] or char in columns[col] or char in squares[(row//3, col//3)]:
                    return False

                rows[row].add(char)
                columns[col].add(char)
                squares[(row//3, col//3)].add(char)

        return True

# 9.35 -> 10 min to solve