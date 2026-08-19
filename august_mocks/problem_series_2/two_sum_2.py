# 4.13
# given sorted array and target, return 1 indexed positions of two numbers that add up to target.
# use two pointers, left and right -> add numbers at this positions -> do binary search

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Find two numbers that add up to target number in given sorted array and return their 1-index positions as list.

        Args:
            nums: sorted integer array
            target: target number

        Returns:
            list containing index of two numbers that add up to target

        Time: O(n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:

            val = nums[left] + nums[right]

            if val < target:
                left += 1
            elif val > target:
                right -= 1
            else:
                return [left + 1, right + 1]



s = Solution()
assert s.twoSum([2,7,11,15], 9) == [1,2]
assert s.twoSum([1,2,3,4,4,9,56,90], 8) == [4,5]
assert s.twoSum([-1,0,2,5,9,12], 7) == [3,4]
assert s.twoSum([1,2], 3) == [1,2]
assert s.twoSum([0,0,3,4], 0) == [1,2]
print("passed")

# 4.23 -> 10 min to solve