# 7.12

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Find the target number in the matrix.

        Args:
            matrix (list[list[int]]): m*n matrix
            target (int): integer to search for

        Returns:
            bool: True if target is found, else False

        Time: O(log(m*n)) - m,n = m*n matrix
        Space: O(1)
        """

        # treat is as flat array
        rows = len(matrix)
        columns = len(matrix[0])
        left = 0
        right = rows*columns-1

        while left <= right:
            index = (left + right) // 2
            row = index // columns
            col = index % columns
            num = matrix[row][col]

            if num == target:
                return True

            if num < target:
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
print('passed')