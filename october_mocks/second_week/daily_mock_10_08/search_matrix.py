# 10.44

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Search the target number in given m*n matrix.

        Args:
            matrix (list[list[int]]): given m*n matrix
            target (int): number to search for

        Returns:
            bool: True if the target is found, else False

        Time complexity: O(log (m*n)) - m, n = number of rows and columns in given matrix

        Space complexity: O(1)
        """

        # treat m*n matrix as flat array

        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows * columns - 1

        while left <= right:
            index = (left + right) // 2
            row = index // columns
            col = index % columns

            if target == matrix[row][col]:
                return True

            if target > matrix[row][col]:
                left = index + 1
            else:
                right = index - 1

        return False

# 10.56 -> 12 minutes to solve problem
# git commit -> feat: add search in 2D matrix solution

s = Solution()
m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
assert s.searchMatrix(m, 3) == True
assert s.searchMatrix(m, 13) == False
assert s.searchMatrix(m, 1) == True
assert s.searchMatrix(m, 60) == True
assert s.searchMatrix(m, 10) == True
assert s.searchMatrix(m, 23) == True
assert s.searchMatrix(m, 8) == False
assert s.searchMatrix(m, 0) == False
assert s.searchMatrix(m, 100) == False
assert s.searchMatrix([[1]], 1) == True
assert s.searchMatrix([[1]], 2) == False
assert s.searchMatrix([[1, 3]], 3) == True
assert s.searchMatrix([[1], [3]], 3) == True
assert s.searchMatrix([[1], [3]], 2) == False
big = [[r * 1000 + c for c in range(1000)] for r in range(1000)]
assert s.searchMatrix(big, 999999) == True
assert s.searchMatrix(big, -1) == False
