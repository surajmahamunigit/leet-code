# algorithm
# given rotated sorted array and we have to find out min number present in array
# rotated array property -> if mid number > array[right_index] -> minimum is on left of mid

class Solution:
    def min_in_rotated_sorted_array(self, nums: list[int]) -> int:
        """Find minimum number present in given array.

        Args:
            nums: rotated sorted integer array

        Return:
            minimum number present in the array

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """


        left = 0
        right = len(nums) - 1

        while left < right:
            mid_index = (left + right) // 2
            mid_num = nums[mid_index]

            if mid_num > nums[right]:
                left = mid_index + 1
            else:
                right = mid_index

        return nums[left]

s = Solution()
assert s.min_in_rotated_sorted_array(nums = [3,4,5,6,1,2]) == 1
assert s.min_in_rotated_sorted_array(nums = [4,5,0,1,2,3]) == 0

print("passed")