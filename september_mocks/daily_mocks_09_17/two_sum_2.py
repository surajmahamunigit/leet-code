# 6.05

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Find the indices of two numbers that add up to target.

        Args:
            nums (list[int]): given ascending order sorted array of integers
            target (int): target number

        Returns:
            list[int]: 1-indexed indices corresponding to each number

        Time: O(n) - n = len(nums)

        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return [left+1, right+1]

        return []

s = Solution()
print(s.twoSum([2,7,11,15], 22))

