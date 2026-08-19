# 9.13
# given m*n array sorted in ascending order, asked to find target and return True, else False
# treat m*n matrix as flat array and then use binary search

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Find target number in given m*n matrix and return True, else False.

        Args:
            matrix: m*n integer array sorted in ascending order
            target: target number

        Returns:
            True if target is found, else False

        Time: O(log m*n) - m*n = size of board
        Space: O(1)
        """

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n - 1

        while left <= right:
            index = (left + right) // 2
            row = index // n                        # columns
            col = index % n
            curr_num = matrix[row][col]

            if curr_num > target:
                right = index - 1
            elif curr_num < target:
                left = index + 1
            else:
                return True

        return False

# 9.21 -> 8 min to solve