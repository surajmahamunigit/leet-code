# 10.33
# given m*n sorted matrix, asked to find if target exists
# treat m*n matrix as m*n length flat array -> find middle
# binary search

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Find out if given target exists in given matrix.

        Args:
            matrix: m*n matrix
            target: number to look for

        Returns:
            True if target is found, else False

        Time: O(log (m*n))
        Space: O(1)
        """

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n - 1

        while left <= right:
            index = (left + right) // 2
            row = index // n
            col = index % n
            curr_num = matrix[row][col]

            if curr_num < target:
                left = index + 1
            elif curr_num > target:
                right = index - 1
            else:
                return True

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

# 10.41 -> 8 min to solve