# 11.16
# givens nums integer array, asked to find longest consecutive sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Find the length of longest consecutive sequence in the nums.

        Args:
            nums: integer array

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
            while num + length in nums_set:
                length += 1
                longest = max(longest, length)

        return longest

s = Solution()
res = s.longestConsecutive([-1,1,2,3,4,5])
print(res)

# 11.22 -> 6 min to solve