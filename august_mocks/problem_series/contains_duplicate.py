# 11.39
# given nums array, returns true or false depends on duplicate number in array
# array pattern

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """Determine if the given list contains duplicate number.

        Args:
            nums: list of integers

        Returns:
            True if list contains duplicate number else False

        Time: O(n) - n = len(nums)
        Space: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False

s = Solution()
assert s.containsDuplicate([1,2,3,1]) == True
assert s.containsDuplicate([1,2,3,4]) == False
assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
assert s.containsDuplicate([]) == False
assert s.containsDuplicate([1]) == False
print("passed")

# 11.44 -> 6 minutes to solve
