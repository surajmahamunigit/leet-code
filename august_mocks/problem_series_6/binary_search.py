# 10.21
# given distinct number sorted array and target. asked to find out target number and return its index or -1

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the index of target number.

        Args:
            nums: sorted array with distinct numbers
            target: number to look for
        Returns:
            index of target number

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (left + right) // 2
            val = nums[index]

            if val > target:
                right = index - 1
            elif val < target:
                left = index + 1
            else:
                return index

        return -1

# 10.30 -> 9 min to solve
