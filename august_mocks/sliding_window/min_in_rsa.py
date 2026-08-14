# 12.08

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Find minimum number in given array.

        Args:
            nums: rotated sorted array

        Returns:
            smallest number in given array

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        # find middle -> compare
        left = 0
        right = len(nums) - 1

        while left < right:
            mid_index = (left + right) // 2
            mid_num = nums[mid_index]

            if mid_num > nums[right] :
                left = mid_index + 1
            else:
                right = mid_index

        return nums[left]

s = Solution()
assert s.findMin([3,4,5,1,2]) == 1
assert s.findMin([4,5,6,7,0,1,2]) == 0
assert s.findMin([11,13,15,17]) == 11    # no rotation
assert s.findMin([1]) == 1
assert s.findMin([2,1]) == 1
print("passed")

# 12.15 -> 7 min to finish