# 11.39

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Return indices of two numbers that add up to target.

        Args:
            nums: list of integers
            target: target sum

        Returns:
            list of indices of two numbers

        Time: O(n) - n = len(nums)
        Space: O(n)
        """
        seen = {}

        for index, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], index]
            else:
                seen[num] = index

        return []

s = Solution()
assert s.twoSum([2,7,11,15], 9) == [0,1]
assert s.twoSum([3,2,4], 6) == [1,2]
assert s.twoSum([3,3], 6) == [0,1]
print("passed")

# 11.44 -> 5 min to solve