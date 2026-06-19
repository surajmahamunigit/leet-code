"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        ROWS= len(matrix)
        COLS = len(matrix[0])

        top, bottom = 0, ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1

            elif target < matrix[row][0]:
                bottom = row - 1

            else:
                break

        if not (top <= bottom):
            return False

        row = (top + bottom) // 2
        left, right = 0, COLS - 1
        while left <= right:
            m = (left +right) // 2

            if target > matrix[row][m]:
                left = m + 1

            elif target < matrix[row][m]:
                right = m - 1

            else:
                return True

        return False

result = Solution().searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 22)
print  (result)

