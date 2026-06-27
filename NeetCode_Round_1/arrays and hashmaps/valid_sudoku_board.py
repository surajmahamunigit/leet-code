
import collections
class Solution:
    def validSudokuBoard(self, board: list[list[str]]) -> bool:
        """
        Args:
             board: sudoku board

        Return:
            True if sudoku board is valid, otherwise False

        Time: O(1) - 9*9 = 81 elements to look up
        Space: O(n) - 81 elements to store
        """

        rows = collections.defaultdict(set)
        columns= collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                if num == ".":
                    continue

                if num in rows[r] or num in columns[c] or num in squares[(r//3, c//3)]:
                    return False

                rows[r].add(num)
                columns[c].add(num)
                squares[(r//3, c// 3)].add(num)

        return True

board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
result = Solution().validSudokuBoard(board)
print(result)