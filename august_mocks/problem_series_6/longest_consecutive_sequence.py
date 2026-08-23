# 1.37
# given list of numbers and asked to find out the length of the longest consecutive sequence
# for every number check if its previous number is in nums_set
# if yes -> continue
# if not -> start counting length from that number and keep track of longest one found

class Solution:
    def longestConsecutiive(self, nums: list[int]) -> int:
        """Find the length of longest consecutive elements in nums.

        Args:
            nums: list of integers

        Returns:
            length of longest consecutive number sin given nums

        Time: O(n) - n = length of nums
        Space: O(n)
        """

        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue

            length = 0
            while num + length in nums_set:
                length += 1
                longest = max(length, longest)

        return longest

# 1.47 -> 10 min to solve