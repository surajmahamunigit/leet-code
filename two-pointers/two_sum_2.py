"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use
O
(
1
)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]

Time: O(n)
Space: O(1)
"""

class Solution:
    def twoSum(self, numbers: list[int], target:int) -> list[int]:

        left_index = 0
        right_index = len(numbers) - 1

        while left_index < right_index:

            total_sum = numbers[left_index] + numbers[right_index]

            # Check if total_sum > target
            if total_sum > target:
                right_index -= 1

            # Check if total_sum < target
            elif total_sum < target:
                left_index += 1

            else:
                return [left_index + 1, right_index + 1]

        return []



result = Solution().twoSum([2,7,11,15], 9)
print(result)