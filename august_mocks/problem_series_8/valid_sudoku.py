# 1.30

from collections import defaultdict

class Solution:
    def validSudoku(self, board: list[list[int]]) -> bool:
        """Find out if the given sudoku board is valid or not.

        Args:
            board: given 9*9 sudoku board

        Returns:
            True if board is valid, else False

        Time: O(1) - 9*9 possible combinations
        Space: O(1)
        """

        rows = defaultdict(list)
        columns = defaultdict(list)
        squares = defaultdict(list)

        for row in range(9):
            for col in range(9):
                char = board[row][col]

                if char == ".":
                    continue

                if char in rows[row] or char in columns[col] or char in squares(row//3, col//3):
                    return False

                rows[row].append(char)
                columns[col].append(char)
                squares[(row//3, col//3)].append(char)

        return True

