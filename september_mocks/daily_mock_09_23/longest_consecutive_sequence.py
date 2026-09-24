# 7.18

class Solution:
    def longest_consecutive(self, nums: list[int]) -> int:
        """Find the longest consecutive sequence in the given array.

        Args:
            nums (list[int]): list of integers

        Returns:
            int: longest consecutive sequence in given array

        Time: O(n) - n = len(nums)

        Space: O()
        """

        longest = 0

        nums_set = set(nums)
        for index in range(len(nums_set)):

            if nums[index] - 1 in nums_set:
                continue

            length = 0
            while nums[index] + length in nums_set:
                length += 1
                longest = max(longest, length)

        return longest

s = Solution()

print(s.longest_consecutive(nums = [2,20,4,10,3,4,5]))
print(s.longest_consecutive(nums = [0,3,2,5,4,6,1,1]))