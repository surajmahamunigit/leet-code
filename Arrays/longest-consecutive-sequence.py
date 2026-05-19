"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Time = O(n)
Space = O(n)

"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        num_set = set(nums)
        longest_sequence = 0

        for num in nums:

            # Check if the num is start of a sequence
            if (num - 1) not in num_set:

                length = 0
                while(num+length in num_set):
                    length += 1

                longest_sequence = max(longest_sequence, length)

        return longest_sequence


longest_consecutive_sequence = Solution().longestConsecutive([2, 20, 4, 10, 3, 4, 5])
print(longest_consecutive_sequence)