# 11.49

class Solution:
    def longestConsecutiveSequence(self, nums: list[int]) -> int:
        """Find the longest consecutive sequence in given array.

        Args:
            nums: given integer array

        Returns:
            length of longest consecutive sequence

        Time: O(n) - n = len(nums)
        Space: O(n)
        """
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue

            length = 0
            while (num + length) in nums_set:
                length += 1
                longest = max(longest, length)

        return longest

s = Solution()
res = s.longestConsecutiveSequence([0,3,2,5,4,6,1,1])
print(res)

# 11.56 -> 7 min to solve