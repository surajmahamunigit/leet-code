# 7.28
#given -> rotated sorted array with all unique numbers
# asked -> to find smallest number

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Find the smallest integer in given rotated sorted array.

        Args:
            nums (list[int]): given rotated sorted array

        Returns:
            int: smallest integer in given array

        Time complexity: O(log n) - n = len(nums)

        Space complexity: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid_index = (left + right) // 2

            # smallest is on right if mid_index
            if nums[mid_index] > nums[right]:
                left = mid_index + 1
            else:
                right = mid_index

        return nums[left]

# 7.37 -> 9 minutes to solve problem
# git commit -> feat: add find minimum in rotated sorted array solution

