# 11.18

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Find the target number in given matrix.

        Args:
            matrix: m*n matrix array sorted in ascending order
            target: number to search for

        Returns:
            True if number is found, else False

        Time: O(log (m*n)) - m,n = number of rows and columns in matrix
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
res = s.searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10)
print(res)

# 11.24 -> 6 min to solve