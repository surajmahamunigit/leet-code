# 3.32

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find a target number and return its index.

        Args:
            nums (list[int]): sorted integer array
            target (int): target integer

        Returns:
            int: index of target number

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (left + right) // 2
            num = nums[index]

            if num == target:
                return index

            if num < target:
                left = index + 1
            else:
                right = index - 1

        return - 1

s = Solution()
assert s.search([-1,0,3,5,9,12], 9) == 4
assert s.search([-1,0,3,5,9,12], 2) == -1
assert s.search([-1,0,3,5,9,12], 22) == -1
assert s.search([-1,0,3,5,9,12], -2) == -1
assert s.search([-1], -1) == 0
assert s.search([-1], 1) == -1
print('passed')