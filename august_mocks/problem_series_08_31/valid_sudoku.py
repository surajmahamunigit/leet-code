# 10.31

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[int]]) -> bool:
        """Find the given board is valid or not.

        Args:
            board: 9*9 sudoku board

        Returns:
             True if the board is valid else False

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


