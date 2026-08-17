# 6.42

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find out target number and return its index, else -1.

        Args:
            target: number to look for
            nums: rotated sorted array

        Returns:
            if found index of number, else -1

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_num = nums[mid_index]

            if mid_num == target:
                return mid_index

            if nums[left] <= mid_num:
                if nums[left] <= target < mid_num:
                    right = mid_index - 1
                else:
                    left = mid_index + 1
            else:
                 if mid_num < target <= nums[right]:
                     left = mid_index + 1
                 else:
                     right = mid_index - 1

        return -1

s = Solution()
assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([4,5,6,7,0,1,2], 3) == -1
assert s.search([1], 1) == 0
assert s.search([1], 0) == -1
assert s.search([5,1,3], 5) == 0
assert s.search([1,2,3,4,5], 5) == 4
print("passed")

# 6.56 -> 14 min to finish
