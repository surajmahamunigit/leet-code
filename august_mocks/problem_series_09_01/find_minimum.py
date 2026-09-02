# 5.27

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Find minimum number in given rotated sorted array.

        Args:
            nums: rotated sorted array

        Returns:
            smallest number in the given array

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid_index = (left+ right) // 2
            val = nums[mid_index]

            if val >= nums[right]:
                left = mid_index + 1
            else:
                right = mid_index

        return nums[left]

s = Solution()
assert s.findMin([3,4,5,1,2]) == 1
assert s.findMin([4,5,6,7,0,1,2]) == 0
assert s.findMin([11,13,15,17]) == 11
assert s.findMin([1]) == 1
assert s.findMin([2,1]) == 1
print('passed')

# 5.36 -> 9 min