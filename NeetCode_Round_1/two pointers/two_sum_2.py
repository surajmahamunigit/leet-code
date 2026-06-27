class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Important Personal Note: Input array is sorted thats why we are using two pointers, otherwise use hashmap/dict.

        Args:
            numbers: List of integers
            target: target sum

        Returns:
            list[int]: indices of two elements that add up to target

        Time: O(n) - for n integers
        Space: O(1) - no extra space
        """
        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [left+1, right+1]

        return []

result = Solution().twoSum([1,2,3,4,5], 7)
print(result)