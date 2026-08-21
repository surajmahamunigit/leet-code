# 4.31
# given rotated sorted array and target, and aksd to find index of target number
# find mid -> then check if left side is roted
# then check if right side sorted

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Return the index of target number.

        Args:
            nums: rsa array
            target: number to search for

        Returns:
            index of target number else, -1

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (left + right) // 2
            val = nums[index]

            if val == target:
                return index

            # left side sorted
            if nums[left] <= val:
                if nums[left] <= target < val:
                    right = index - 1
                else:
                    left = index + 1

            # if right side is sorted
            else:
                if val < target <= nums[right]:
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
print("passed")

# 4.44 -> 13 min to solve