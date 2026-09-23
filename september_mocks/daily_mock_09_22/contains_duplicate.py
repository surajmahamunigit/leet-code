# 9.16

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        """Find out if the given inter array contains a duplicate.

        Args:
            nums (list[int]): list of integers

        Returns:
            bool: True if the given inter array contains a duplicate else False.

        Time: O(n) - n = len(n)

        Space: O(n)
        """

        seen = set()

        for num in nums:

            if num in seen:
                return True

            seen.add(num)

        return False