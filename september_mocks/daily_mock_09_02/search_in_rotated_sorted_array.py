# 4.06

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the target number and return its index.

        Args:
            nums list[int]: rotated sorted array
            target int: target number

        Returns:
             index of target number if found, else -1

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """
        # [4,5,6,7,0,1,2]


        left = 0
        right = len(nums) - 1

        while left <= right:

            index = (left + right) // 2
            val = nums[index]

            if val == target:
                return index

            # if left of index is sorted
            if nums[left] <= val:
                if nums[left] <= target < val:
                    right = index - 1
                else:
                    left = index + 1
            # right side of index is sorted
            else:
                if val < target <= nums[right]:
                    left = index + 1
                else:
                    right = index - 1

        return - 1

s = Solution()
assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([4,5,6,7,0,1,2], 3) == -1
assert s.search([1], 1) == 0
assert s.search([1], 0) == -1
assert s.search([5,1,3], 5) == 0
assert s.search([1,2,3,4,5], 5) == 4
print('passed')

# 4.35 -> 29 min
# keep this problem on our repetition list for next 2 days