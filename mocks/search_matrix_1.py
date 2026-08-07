# algorithm
# given m*n array and we are asked to return True if target number is in matrix, else False
# lets treat m*n 2d matrix as flat array. left = 0, right = len(matrix) * len(matrix[0]) - 1
# find mid_index = (left + right) // 2, then row = (mid_index // len(matrix[0]), col = (mid_index % len(matrix[0]))
# mid_num = matrix[row][col]
# if mid_num == target -> return True
# else if min_num < target left = mid_index + 1
# else right = mid_index - 1
# in end return False

class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        """Find if target number exist in given m*n matrix.

        Args:
            matrix: m*n integer array
            target: target number to look for in matrix

        Returns:
             True if target exists in given matrix, else False

        Time: O(n log n)
        Space: O(1)
        """

        left = 0
        rows = len(matrix)
        columns = len(matrix[0])
        right = rows * columns - 1

        while left <= right:

            mid_index = (left + right) // 2
            row = mid_index //  columns
            col = mid_index % columns
            mid_num = matrix[row][col]

            if mid_num == target:
                return True

            elif mid_num < target:
                left = mid_index + 1

            else:
                right = mid_index - 1

        return False


s = Solution()
assert s.search_matrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10) == True
assert s.search_matrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15) == False
print("passed")