# algorithm
# given is m*n array sorted ascending order and we have to find if target num exist in or not
# treat m*n array as flat array of 0 - (m*n - 1) array
# find mid_index, convert to matrix[row][[col] -> compare with target, if same return true
# if target > mid_num -> left = mid_index + 1
# else right = mid_index - 1
# in end return False

class Solution:
    def search_matrix(self, matrix: list[int], target: int) -> bool:
        """Find if target number exist in nums.

        Args:
            target: target integer
            matrix: m*n sorted array

        Returns:
            True if target is in nums, else False

        Time: O(log m*n) - n = rows, m = columns
        Space: O(1)
        """
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid_index = (left + right) // 2
            row = mid_index // len(matrix[0])
            col = mid_index % len(matrix[0])
            mid_num = matrix[row][col]

            if target == mid_num:
                return True
            elif target > mid_num:
                left = mid_index + 1
            else:
                right = mid_index - 1

        return False

s = Solution()
#res = s.search_matrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10)
res = s.search_matrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15)
print(res)

