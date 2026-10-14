# 7.46

# given -> integer array
# asked -> to find longest sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Find the length of longest consecutive sequence in the given array.

        Args:
            nums (list[int]): given integer array

        Returns:
            int: length of longest consecutive sequence in the given array

        Time complexity: O(n) - n = len(nums)

        Space complexity: O(n)
        """

        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 in num_set:
                continue
            else:
                length = 0
                while num + length in num_set:
                    length += 1
                    longest = max(longest, length)

        return longest

# 8.03 - > 17 minutes to solve problem
# git commit -> feat: add longest consecutive sequence solution

import random

s = Solution()
assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
assert s.longestConsecutive([1, 0, 1, 2]) == 3
assert s.longestConsecutive([]) == 0
assert s.longestConsecutive([1]) == 1
assert s.longestConsecutive([5, 5, 5]) == 1
assert s.longestConsecutive([1, 3, 5, 7]) == 1
assert s.longestConsecutive([-1, -2, -3, 0, 1]) == 5
assert s.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7
assert s.longestConsecutive([10, 5, 12, 3, 55, 30, 4, 11, 2]) == 4
assert s.longestConsecutive([1, 2, 0, 1]) == 3
assert s.longestConsecutive([-5, -4, -3, -2, -1]) == 5
assert s.longestConsecutive([1000000000, -1000000000]) == 1
assert s.longestConsecutive([0, -1]) == 2
big = list(range(100000)); random.Random(1).shuffle(big)
assert s.longestConsecutive(big) == 100000
gap = list(range(0, 50000)) + list(range(60000, 110000)); random.Random(2).shuffle(gap)
assert s.longestConsecutive(gap) == 50000