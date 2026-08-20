# 12.08
# given rotated sorted array and asked to find minimum number in it.
# we always have nums[left], nums[middle], nums[right]
# if nums[middle] > nums[right] -> right side is sorted -> left = middle + 1
# else -> right = middle
# binary sort pattern

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Find smallest number in given rotated sorted array.

        Args:
            nums: given rotated sorted array

        Returns:
            smallest number in the rotated sorted array

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            index = (left + right) // 2
            val = nums[index]

            if val > nums[right]:
                left = index + 1
            else:
                right = index

        return nums[left]

s = Solution()

assert s.findMin([3,4,5,1,2]) == 1
assert s.findMin([4,5,6,7,0,1,2]) == 0
assert s.findMin([11,13,15,17]) == 11
assert s.findMin([1]) == 1
assert s.findMin([2,1]) == 1
print("passed")

# 12.18 -> 10 min to solve