# 4
# given ascending sorted array, asked to return 1-indexed positions of two numbers that add up to target
# use two pointer solution

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Find two numbers from given list that add up to target and return their 1-indexed position.

        Args:
            numbers: list of sorted numbers

        Returns:
            1-indexed position two numbers that add up to target

        Time: O(n) - n = len(numbers)
        Space: O(1)
        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return []

# 4.06 -> 6 min to solve