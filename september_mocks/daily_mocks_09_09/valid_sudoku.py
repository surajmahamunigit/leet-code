# 12.12

from collections import defaultdict
class Solution:
    def validSudoku(self, board: list[list[str]]) -> bool:
        """Find out if the given board is valid or not.

        Args:
            board (list[list[str]]): 9*9 sudoku board

        Returns:
              bool: True if the board is valid, False otherwise

        Time: O(1)
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

# 12.17