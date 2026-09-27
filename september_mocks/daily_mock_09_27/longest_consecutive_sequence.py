# 11.56

class Solution:
    def longest_sequence(self, nums: list[int]) -> int:
        """Find the longest consecutive sequence in given array.

        Args:
            nums (list[int]): list of integers

        Returns:
            int: longest consecutive sequence

        Time: O(n) - len(nums)

        Space: O(n)
        """

        # nums = [2,20,4,10,3,4,5]
        longest = 0

        nums_set = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue

            length = 0
            while num + length in nums_set:
                length += 1
                longest = max(longest, length)

        return longest

s = Solution()
print(s.longest_sequence([1,2,3,4,5]))
print(s.longest_sequence([1,3,4,5]))
print(s.longest_sequence([]))