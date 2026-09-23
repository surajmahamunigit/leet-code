# 9.26

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """Find two numbers that add up to the target and return their indices.

        Args:
            nums (list[int]): given integer array
            target (int): target sum

        Returns:
            list[int]: indices of two numbers that add up to target

        Time: O(n) - n - len(nums)

        Space: O(n)
        """

        seen = {}

        for index in range(len(nums)):
            compliment = target - nums[index]

            if compliment in seen:
                return [seen[compliment], index]

            seen[nums[index]] = index

        return []
