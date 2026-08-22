# 5.12
# given unsorted array and asked to find out length of sequence in nums that doesnt have repeated numbers.


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """find length of longest consecutive sequence in nums.

        Args:
            nums: list of integers

        Returns:
            length of longest consecutive sequence in nums

        Time: O(n) - n = len(nums)
        Space: O(n)
        """
        longest = 0

        nums_set = set(nums)
        left = 0

        for num in nums_set:

            # if previous number exist in nums, skip
            if num - 1 in nums_set:
                continue

            length = 0
            while num + length in nums_set:
                length += 1
                longest = max(longest, length)

        return longest

s = Solution()

assert s.longestConsecutive([100,4,200,1,3,2]) == 4
assert s.longestConsecutive([1,2,3,4,5]) == 5
assert s.longestConsecutive([10,1,3,5]) == 1
assert s.longestConsecutive([]) == 0
print("passed")

# 5.30 -> 18 min to solve
# add this problem on repetition list for next two days