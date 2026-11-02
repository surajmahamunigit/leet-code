# 8.11

from collections import defaultdict

class Solution:
    def valid_sudoku(self, sudoku: list[list[str]]) -> bool:
        """Find the given sudoku is valid or not.

        Args:
            sudoku (list[list[str]]): given 9*9 sudoku board

        Returns:
            bool: True if the sudoku is valid, False otherwise

        Time complexity: O(1)

        Space complexity: O(1)
        """
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(sudoku)):
            for col in range(len(sudoku[0])):
                char = sudoku[row][col]

                if char == ".":
                    continue

                if char in rows[row] or char in columns[col] or char in squares[(row//3, col//3)]:
                    return False

                rows[row].add(char)
                columns[col].add(char)
                squares[(row//3, col//3)].add(char)

        return True

# 8.21 -> 10 minutes to solve the problem

# git commit -> feat: add valid sudoku solution