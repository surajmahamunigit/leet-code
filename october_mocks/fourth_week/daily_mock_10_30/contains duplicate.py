# 9.51

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        """Find out if the given list of integer contains duplicate number.

        Args:
            nums (List[int]): list of integers

        Returns:
            bool: True if the list contains duplicate number, else False

        Time complexity: O(n) - n = len(nums)

        Space complexity: O(n)
        """

        seen = set()

        for val in nums:
            if val in seen:
                return True

            seen.add(val)

        return False

s = Solution()

def check(values, expected):
    result = s.contains_duplicate(values)
    assert result == expected

check([], False)
check([1], False)
check([1,2], False)
check([1,2,1], True)
print("all passed")