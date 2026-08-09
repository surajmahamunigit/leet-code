# algorithm
# we are given ascending sorted array and we have to find out two numbers that add to target num and return their indices
# left = 0, right = len(nums)-1
# while left < right
# caclulate curr_sum = nums[left] + nums[right] -> if curr_sum > target -> move right inward, else mover left forward
# return [left+1, right+1] because its 1_index array

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """Find indices of two numbers that add upto target.

        Args:
            nums: sorted integer array
            target: target sum of two numbers

        Returns:
            indices of two numbers that add upto target

        Time: O(n) - n = len(nums)
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum > target:
                right -= 1
            else:
                left += 1

        return []

s = Solution()
res = s.two_sum(nums = [1,2,3,4], target = 3)
print(res)
