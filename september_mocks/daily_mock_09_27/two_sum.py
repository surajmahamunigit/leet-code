# 1.39

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """Find indices of two numbers that add up to the target.

        Args:
            nums (list[int]): list of integers
            target (int): target number

        Returns:
             list[int]: list of indices of two numbers that add up to the target

        Time: O(n) -  n = len(nums)

        Space: O(n)
        """

        # nums = [3,4,5,6], target = 7

        seen = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]

            seen[num] = index

        return []

s = Solution()
print(s.two_sum([2, 7, 11, 15], 90))
print(s.two_sum([-1, -1], -2))
