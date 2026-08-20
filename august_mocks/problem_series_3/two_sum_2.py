# 11.16
# given sorted array and target, asked to find out 1-indexed positions of two numbers that add up to target number
# given array is sorted -> use two pointers approach to find two numbers

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Find two numbers that add up to target and return their 1-indexed positions.

        Args:
            nums: sorted integer array
            target: target number

        Returns:
            list of 1-indexed positions of two numbers that add up to target

        Time: O(n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right]

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
assert s.twoSum([-1,0,2,5,9,12], 7) == [3,4]
assert s.twoSum([1,2], 3) == [1,2]
assert s.twoSum([0,0,3,4], 0) == [1,2]
print("passed")

# 11.22 -> 6 min to solve