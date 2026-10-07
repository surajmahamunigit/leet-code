# 10.16

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Search target number in the given rotated sorted integer array and return its index if found, else -1.

         Args:
             nums (list[int]): rotated sorted integer array
             target (int): target number to search in nums

         Returns:
             int: index of the target number if found, else -1

         Time complexity: O(log n) - n = len(nums)

         Space complexity: O(1)
         """

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2

            if target == nums[mid_index]:
                return mid_index

            # left side of mid_index is sorted
            if nums[left] <= nums[mid_index]:
                if nums[left] <= target < nums[mid_index]:
                    right = mid_index - 1
                else:
                    left = mid_index + 1

            # right side of mid_index is sorted
            else:
                if nums[mid_index] < target <= nums[right]:
                    left = mid_index + 1
                else:
                    right = mid_index - 1

        return -1

# 10.25 -> 9 minutes to solve the problem
    # git commit -> feat: add search in rotated sorted array solution