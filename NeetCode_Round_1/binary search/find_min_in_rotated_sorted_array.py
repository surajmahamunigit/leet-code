class Solution:
    def findMin(self, nums: list[int]) -> int:

        # Binary search -> left, right, middle
        # rules: if nums[middle] > nums[right]: left = mid + 1, otherwise right = mid

        left = 0
        right = len(nums) - 1

        while left < right:         # remeber its left < right, despite binary search pattern

            middle = (left + right) // 2
            mid_num = nums[middle]

            if mid_num > nums[right]:
                left = middle + 1          # remember its mid + 1

            else:
                right = middle             # its mid, not mid - 1. otherwise we might miss middle

        return nums[left]               # remember


