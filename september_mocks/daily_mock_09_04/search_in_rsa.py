# 1.16

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the target number in given rotated sorted array.


        Args:
            nums (list[int]): rotated sorted array
            target (int): target number to look for

        Returns:
            int: index of target number if found else -1

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        # [5, 6, 7, 0, 1, 2, 3, 4]

        left = 0
        right = len(nums) - 1

        while left <= right:

            index = (left + right) // 2

            if nums[index] == target:
                return index

            # if left of index is sorted
            if nums[left] <= nums[index]:
                if nums[left] <= target < nums[index]:
                    right = index - 1
                else:
                    left = index + 1
            # if right of index is sorted
            else:
                if nums[index] < target <= nums[right]:
                    left = index + 1
                else:
                    right = index - 1

        return -1

s = Solution()

assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([4,5,6,7,0,1,2], 3) == -1
assert s.search([1], 1) == 0
assert s.search([1], 0) == -1
assert s.search([5,1,3], 5) == 0
assert s.search([1,2,3,4,5], 5) == 4
assert s.search([3,1], 5) == -1

print('passed')