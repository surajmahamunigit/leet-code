# Algorithm
# given nums = [3,4,5,1,2], assume left = 0, right= len(nums) -1 = 4
# while left < right -> mid_index = (left + right) // 2
# if nums[mid_index] > nums[right] -> meaning array is rotated and smaller number will be on right of mid_index -> left = mide_index + 1
# else smaller number is on left of mid_index -> right = mid_index
# return nums[left] or nums[right]

# nums = [3,4,5,1,2]
# left=0, right=4, mid_index = 2 -> nums[mid_index] = 5 -> 5 > 2 -> left = mid_index+1
# left=3, right=4, mid_index = 3 -> nums[mid_index] = 1 -> 1 < 2 -> right=mid_index=3
# left = 3, right = 3 => return nums[left] = 1

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Find the minimum number in the rotated sorted array.

        Args:
            nums: list of integers sorted and rotated

        Returns:
            smallest number in the array

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:                     # in end, left and right will be same and that will break this loop
            mid = (left + right) // 2
            mid_num = nums[mid]

            # if mid_num is bigger than nums[right] means smaller number is on right side of mid_num
            if mid_num > nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[right]

s = Solution()
assert s.findMin([3,4,5,1,2]) == 1
assert s.findMin([4,5,6,7,0,1,2]) == 0
print("passed")
