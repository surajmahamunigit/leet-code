# 4.29

class Solution:
    def longest_sequence(self, nums: list[int]) -> int:
        """Find length of longest consecutive sequence in nums.

        Args:
            nums: integer array

        Returns:
            length of longest consecutive sequence

        Time: O(n) - n = len(nums)
        Space: O(n)
        """
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            length = 0
            if (num - 1) not in nums_set:

                while (num + length) in nums_set:
                    length += 1

                longest = max(longest, length)

        return longest

s = Solution()
res = s.longest_sequence(nums = [0,3,2,5,4,6,1,1])

print(res)

# 4.39 -> 10 min