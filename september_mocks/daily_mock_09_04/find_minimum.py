# 8.38

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Find the smallest number in given array.

        Args:
            nums (list[int]): given rotated sorted array

        Returns:
            int: smallest number in given array

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            index = (left + right) // 2

            if nums[index] > nums[right]:
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
print('passed')