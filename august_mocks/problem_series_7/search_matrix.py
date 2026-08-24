# 12.45
# given m*n matrix which is sorted in ascending order. we are asked to find out if target number exist in it or not


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Find out if the given number exist in m*n matrix.

        Args:
            matrix: m*n sorted matrix
            target: number to search for

        Returns:
            True if target number found, else False

        Time: O(m*n) - m, n = number of rows and columns in matrix
        Space: O(1)
        """
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1

        while left <= right:
            index = (left + right) // 2
            row = index // len(matrix[0])
            col = index % len(matrix[0])
            val = matrix[row][col]

            if val == target:
                return True

            if val < target:
                left += 1
            else:
                right -= 1

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

# 12.54 -> 10 min to solve