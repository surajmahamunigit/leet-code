# 7.46

class Solution:
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        """Find the two numbers that add up to the target and return their 1-indexed positions.

        Args:
            numbers (list[int]): list of integers sorted in ascending order
            target (int): target number

        Returns:
              list[int]: 1-indexed positions of two numbers that add up to target

        Time: O(n) -  n = len(numbers)

        Space:  O(1)
        """

        # numbers = [1,2,3,4], target = 3
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

s = Solution()
print(s.two_sum([2, 7, 11, 15], 9))
print(s.two_sum([1, 2, 3, 4], 3))
print(s.two_sum([], 9))