# 4.46

class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        """Find out if the target number exist in the given matrix or not.

        Args:
            matrix: m*n integer matrix
            target: number to look for within m*n matrix

        Returns:
            bool: True if the target is present in the given matrix, else False

        Time complexity: O(log(m*n)) - m = number of rows, n = number of columns

        Space complexity: O(1)
        """
        rows  = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid_index = (left + right) // 2
            row = mid_index // cols
            col = mid_index % cols
            if matrix[row][col] == target:
                return True

            if matrix[row][col] < target:
                left = mid_index + 1
            else:
                right = mid_index - 1

        return False

s = Solution()

def check(values, target, expected):
    result = s.search_matrix(values, target)
    assert result == expected

check(values = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3, expected = True)
check(values = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13, expected = False)
print("all tests passed")