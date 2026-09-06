# 6.42

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Find the two numbers that sum up to target and returns their 1-indexed positions.

        Args:
            nums (list[int]): given sorted integer array
            target (int): target sum of two numbers

        Returns:
            list[int]: 1-indexed position of two numbers that add up to target

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
                return [left + 1, right + 1]

        return []

s = Solution()
assert s.twoSum([2,7,11,15], 9) == [1,2]
assert s.twoSum([1,2,3,4,4,9,56,90], 8) == [4,5]
assert s.twoSum([-1,0,2,5,9,12], 7) == [3,4]
assert s.twoSum([1,2], 3) == [1,2]
assert s.twoSum([0,0,3,4], 0) == [1,2]
print('passed')