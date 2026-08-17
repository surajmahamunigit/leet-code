# 1.22

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Find two numbers that add up to target and return their 1-indexed position.

        Args:
            numbers: list of integers
            target: target number

        Returns:
            list of 1-indexed position of two numbers that add up to target

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

s = Solution()
assert s.twoSum([2,7,11,15], 9) == [1,2]
assert s.twoSum([1,2,3,4,4,9,56,90], 8) == [4,5]
assert s.twoSum([-1,0,3,5,9,12], 8) == [3,4]
assert s.twoSum([1,2], 3) == [1,2]
assert s.twoSum([0,0,3,4], 0) == [1,2]
print("passed")

# third test case has two possible solution. i think original problem also has unique solution.
# 1.32 -> 10 min to solve