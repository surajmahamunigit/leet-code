# 10.40

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Find out if the given target number exist in the given m*n matrix.

        Args:
            matrix: given m*n matrix
            target: number to search for

        Returns:
            True if the target exists in the given matrix, else False

        Time: O(log(m*n)) - m, n = m*n matrix
        Space: O(1)

        """

        # binary search pattern
        # treat given m*n matrix as flat array

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
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
assert s.searchMatrix(matrix, 3) == True
assert s.searchMatrix(matrix, 13) == False
assert s.searchMatrix(matrix, 1) == True
assert s.searchMatrix(matrix, 60) == True
assert s.searchMatrix([[1]], 1) == True
assert s.searchMatrix([[1,3,5,7]], 7) == True
assert s.searchMatrix([[1],[3],[5],[7]], 5) == True
print("passed")