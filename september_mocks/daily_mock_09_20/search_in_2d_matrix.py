# 6.25

class Solution:
    def search(self, matrix: list[list[int]], target: int) -> bool:
        """Find the target number in given matrix.

        Args:
            matrix (list[list[int]]): 2d matrix in sorted order
            target (int): number to look for

        Result:
            bool: True if found else False

        Time: O(log(m*n)) - m ,n = number of rows and columns

        Space: O(1)
        """

        # treat it as flat array
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols

        while left <= right:
            index = (left + right) // 2

            row = index // cols
            column = index % cols
            num = matrix[row][column]

            if target == num:
                return True

            if num < target:
                left = index + 1
            else:
                right = index - 1

        return False

s = Solution()
print(s.search(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10))
print(s.search(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15))