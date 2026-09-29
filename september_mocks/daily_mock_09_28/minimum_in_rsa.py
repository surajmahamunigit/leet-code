# 9.07

class Solution:
    def min_in_rsa(self, nums: list[int]) -> int:
        """Find minimum in rotated sorted array.

        Args:
            nums (list[int]): integer array in ascending order

        Returns:
            int: minimum in rotated sorted array

        Time complexity: O(log n) - n = len(nums)

        Space complexity: O(1)
        """

        # nums = [3,4,5,6,1,2]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid_index = (left + right) // 2

            if nums[mid_index] >= nums[right]:
                left = mid_index + 1
            else:
                right = mid_index

        return nums[left]

s = Solution()
print(s.min_in_rsa([1,2,3,4,5]))
print(s.min_in_rsa([3,4,5,6,7]))
print(s.min_in_rsa([3,3,3,3]))