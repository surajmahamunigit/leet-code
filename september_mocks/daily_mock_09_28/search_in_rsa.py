# 9.18

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the target number in rotated sorted array and return its index.

        Args:
            nums (list[int]): list of integers sorted in ascending sorted array
            target (int): target number to search for

        Returns:
            int: index of target number in nums, or -1 if target is not found

        Time complexity: O(log n) - n = len(nums)

        Space complexity: O(1)
        """

        # nums = [3,4,5,6,1,2], target = 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2

            if target == nums[mid_index]:
                return mid_index

            # left of mid_index is sorted
            if nums[left] <= nums[mid_index]:
                if nums[left] <= target < nums[mid_index]:
                    right = mid_index - 1
                else:
                    left = mid_index + 1
            # right of mid_index is sorted
            else:
                if nums[mid_index] < target <= nums[right]:
                    left = mid_index + 1
                else:
                    right = mid_index - 1

        return -1

s = Solution()
print(s.search([4,5,6,7,8,9], 5))
print(s.search([4,5,6,7,8,9], 9))
print(s.search([4,5,6,7,8,9], 0))
print(s.search([], 0))