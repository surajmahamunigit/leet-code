class Solution:
    def findMin(self, nums: list[int]) -> int :
        """
        Args:
            nums: list of rotated sorted numbers

        Returns:
            smallest number from given list

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        # Binary Search -> left, right, middle
        # Rule:
        # if nums[middle] > nums[right] -> left = mid + 1, otherwise right = mid

        left = 0
        right = len(nums) - 1

        while left < right:         # Binary search but still -> left < right

            middle = (left + right) // 2

            mid_num = nums[middle]

            if mid_num > nums[right]:
                left = middle + 1

            else:
                right = middle

        return nums[left]

result = Solution().findMin([0,1,2,3,4,5])
print(result)
