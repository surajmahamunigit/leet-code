# 11.04

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Return 1-indexed position of two numbers that add up to target.

        Args:
            nums: sorted array in ascending order
            target: target number

        Returns:
            1-indexed position of two numbers that add up to target

        Time: O(n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:

            val = nums[left] + nums[right]

            if val == target:
                return [left + 1, right + 1]

            if val < target:
                left += 1
            else:
                right -= 1

        return []

s = Solution()
res = s.twoSum([2, 7, 11, 15], 9)
print(res)