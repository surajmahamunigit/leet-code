# 10.40

from collections import defaultdict
class Solution:
    def validSudoku(self, board: list[list[str]]) -> bool:
        """Find out if the given board is valid or not.

        Args:
            board (list[list[str]]): 9*9 sudoku board

        Returns:
            bool: True if the board is valid else False

        Time: O(1)
        Space: O(1)
        """
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue

                if board[row][col] in rows[row] or board[row][col] in columns[col] or board[row][col] in squares[(row//3, col//3)]:
                    return False

                rows[row].add(board[row][col])
                columns[col].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])

        return True

