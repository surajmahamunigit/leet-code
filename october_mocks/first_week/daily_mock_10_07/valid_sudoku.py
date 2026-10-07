# 12.07
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """Find out if the given 9*9 sudoku is valid or not.

        Args:
            board (lst[list[str]]): given 9*9 sudoku board

        Returns:
            bool: True if the board is valid, else False

        Time complexity: O(1) - 9*9 board

        Space complexity: O(1)
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

# 12.13 -> 6 minutes to solve the problem
# git commit -> feat: add valid sudoku solution

