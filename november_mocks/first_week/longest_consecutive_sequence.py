# 8.38

class Solution:
    def longest_consecutive_sequence(self, nums: list[int]) -> int:
        """Find the longest consecutive sequence in the given array.

        Args:
            nums (list[int]): list of integers

        Returns:
            int: length of the longest consecutive sequence

        Time complexity: O(n) - n = len(nums)

        Space complexity: O(n)
        """

        nums_set = set(nums)        # for O(1) lookup
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

def check(values, expected):
    result = s.longest_consecutive_sequence(values)
    assert result == expected

check([0], 1)
check([-1,0,2,3,4], 3)
check([1,2,3,4,5,], 5)
check([1,2,3,1,1], 3)
print("all tests passed")

# 8.56 -> 18 minute sto solve the problem

# git commit -> feat: add longest consecutive sequence solution