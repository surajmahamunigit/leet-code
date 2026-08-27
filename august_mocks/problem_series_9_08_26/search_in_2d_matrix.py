# 7.14

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Find out if the given target exist in given matrix.

        Args:
            matrix: m*n matrix
            target: target number

        Returns:
            True if number is found, else False

        Time: O(log (m*n)) - m,n = number of rows and columns
        Space: O(1)
        """

        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            index = (left + right) // 2
            row = index // len(matrix[0])
            col = index % len(matrix[0])
            val = matrix[row][col]

            if val == target:
                return True

            if val < target:
                left = index + 1
            else:
                right = index - 1

        return False

s = Solution()
res = s.searchMatrix([[1,2,3],[4,5,6],[7,8,9]], 19)
print(res)

# 7.22 -> 8 min to solve