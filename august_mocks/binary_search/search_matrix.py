# 10.13

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """"Find out if target number in given matrix.

        Args:
            matrix: m*n matrix
            target: target number to search for

        Returns:
            True if target is found else False

        Time: O(log p) - p = m*n
        Space: O(1)
        """
        # reate the give m*n matrix as flat array
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid_index = (left + right) // 2
            row = mid_index // len(matrix[0])
            col = mid_index % len(matrix[0])
            mid_num = matrix[row][col]

            if mid_num == target:
                return True

            if mid_num < target:
                left = mid_index + 1
            else:
                right = mid_index - 1

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

# 10.24 -> 11 min to finish