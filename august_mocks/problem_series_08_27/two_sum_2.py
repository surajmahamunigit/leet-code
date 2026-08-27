# 12.40
# given sorted array and asked to find two numbers that add up to target number

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Find and return 1-indexed position of two numbers that add up to target.

        Args:
            numbers: list of sorted integers
            target: integer

        Returns:
            1-indexed position of two numbers that add up to target

        Time: O(n) - n = len(numbers)
        Space: O(1)
        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            val = numbers[left] + numbers[right]

            if val < target:
                left += 1
            elif val > target:
                right -= 1
            else:
                return [left+1, right+1]

        return []

s = Solution()
assert s.twoSum([2,7,11,15], 9) == [1,2]
assert s.twoSum([1,2,3,4,4,9,56,90], 8) == [4,5]
assert s.twoSum([-1,0,2,5,9,12], 7) == [3,4]
assert s.twoSum([1,2], 3) == [1,2]
assert s.twoSum([0,0,3,4], 0) == [1,2]
print("passed")
# 12.46 -> 6 min to solve