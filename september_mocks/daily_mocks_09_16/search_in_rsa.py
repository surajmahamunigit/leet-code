# 7.09

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the target number in rotated sorted array and return its index.

        Args:
            nums (list[int]): given array
            target (int): number to look for

        Returns:
              int: index of the target number if found, else -1

        Time: O(log n) - n = len(nums)

        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (left+right) // 2

            if target == nums[index]:
                return index

            # if left side is sorted
            if nums[left] <= nums[index]:
                if nums[left] <= target < nums[index]:
                    right = index - 1

                else:
                    left = index + 1

            else:
                if nums[index] < target <= nums[right]:
                    left = index + 1

                else:
                    right = index - 1

        return -1
