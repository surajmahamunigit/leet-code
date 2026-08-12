# 4.13
from collections import defaultdict

class Solution:
    def valid_sudoku(self, board: list[list[str]]) -> bool:
        """Find out if given 9*9 sudoku board is valid or not.

        Args:
            board: 9*9 sudoku board with characters

        Returns:
            True if board is valid else False

        Time: O(1) - 9*9 board
        Space: O(1)
        """

        # declare dict to store all rows, columns, and squares
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                sq_index = (row // 3, col // 3)
                num = board[row][col]

                if num ==  ".":
                    continue

                if num in rows[row] or num in columns[col] or num in squares[sq_index]:
                    return False

                rows[row].add(num)
                columns[col].add(num)
                squares[sq_index].add(num)

        return True


board =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
s = Solution()
res = s.valid_sudoku(board)
print(res)

# 4.26 -> 13 min