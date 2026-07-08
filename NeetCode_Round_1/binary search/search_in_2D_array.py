from sqlalchemy.util import column_set


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Args:
            matrix: 2D integer array
            target: number to search within matrix

        Returns:
             returns True if target is found, otherwise returns False

        Time:
        Space:
        """
        # Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
        #
        # Output: true

        rows = len(matrix)
        columns = len(matrix[0])

        total = rows * columns      # total numbers
        left = 0
        right = total - 1

        # binary search (always left <= right)
        while left <= right:

            mid_index = (left + right) // 2

            # find mid_number
            row = mid_index // columns
            column = mid_index % columns    # remember it cold
            mid_num = matrix[row][column]

            if target == mid_num:
                return True
            elif target < mid_num:
                right = mid_index -  1
            else:
                left = mid_index + 1

        return False

result = Solution().searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15)
print(result)