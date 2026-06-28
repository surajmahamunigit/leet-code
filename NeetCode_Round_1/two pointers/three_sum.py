class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Args:
            nums: List of integers

        Returns:
            list[list[int]]: unique triplet that sum to target

        Time: O(n^2) - Outer for-loop and inner two-pointer scan
        Space: O(1) - no extra space
        """
        result = []
        nums.sort()

        # Fix first number
        for index, num in enumerate(nums):

            # If current number (index) and previous number (index - 1) are same, skip
            if index > 0 and num == nums[index - 1]:
                continue

            # Two- pointer for remaining two numbers
            left = index + 1
            right = len(nums) - 1

            while left < right:
                current_sum = num + nums[left] + nums[right]

                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left = left + 1
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
        return result

result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(result)