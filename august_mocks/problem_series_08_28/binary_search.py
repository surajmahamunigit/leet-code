# 9.12

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the given number in nums array.

        Args:
            nums: given sorted array
            target: target number

        Returns:
            return target index if found else -1

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

            if val > target:
                right = index - 1
            elif val < target:
                left = index + 1


        return -1
s = Solution()
assert s.search([-1,0,3,5,9,12], 9) == 4
assert s.search([-1,0,3,5,9,12], 2) == -1
assert s.search([-1,0,3,5,9,12], 22) == -1
assert s.search([-1,0,3,5,9,12], -2) == -1
assert s.search([-1], -1) == 0
assert s.search([-1], 1) == -1
print("passed")

# 9.20 -> 8 min to solve