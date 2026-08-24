# 11.18
# given sorted array and asked to return 1-indexed positions of two numbers that add up to target

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Find the two numbers that ddd up to target and return their 1-indexed position.

        Args:
            nums: list of sorted integers
            target: number to add up to

        Returns:
            list of 1-indexed positions of two numbers that add up to target.

        Time: O(n) - n = len(nums)
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left < right:

            val = nums[left] + nums[right]

            if val == target:
                return [left+1, right+1]

            if val < target:
                left += 1
            else:
                right-= 1

        return []

# 11.27 -> 9 min to solve