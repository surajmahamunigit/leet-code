# 7.23

# given -> integer array, sorted in ascending order
# return 1-indexed position of two numbers that add up to zero.


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Find and return 1-indexed positions of two numbers that add up to target.

        Args:
            numbers (list[int]): list of integers sorted in ascending order
            target (int): target number

        Returns:
            list[int]: 1-indexed position of two numbers that add up to target

        Time complexity: O(n) - n = len(numbers)

        Space complexity: O(1)
        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        return []

# 7.28 -> 5 minute sto finish
# git commit -> feat: add two sum 2 solution

s = Solution()
assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
assert s.twoSum([2, 3, 4], 6) == [1, 3]
assert s.twoSum([-1, 0], -1) == [1, 2]
assert s.twoSum([1, 2], 3) == [1, 2]
assert s.twoSum([0, 0, 3, 4], 0) == [1, 2]
assert s.twoSum([-5, -3, -1, 0, 2, 4], -4) == [2, 3]
assert s.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
assert s.twoSum([5, 25, 75], 100) == [2, 3]
assert s.twoSum([-3, -2, 5, 8], 6) == [2, 4]
assert s.twoSum(list(range(1, 100001)), 199999) == [99999, 100000]