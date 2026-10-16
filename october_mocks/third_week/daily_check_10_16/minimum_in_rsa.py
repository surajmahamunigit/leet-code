# 4
# given -> rotated sorted array with unique integers
# asked -> find out smallest integer in array

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Find the smallest integer in the given rotated sorted array.

        Args:
            nums (list[int]): given rotated sorted array with unique integers

        Returns:
            int: smallest integer in given array

        Time complexity: O(log n) - n = len(nums)

        Space complexity: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid_index = (left + right) // 2

            # right of mid_index has smallest integer
            if nums[mid_index] > nums[right]:
                left = mid_index + 1
            else:
                right = mid_index

        return nums[left]

# 4.09 -> 9 minute sto solve problem
# git commit -> feat: add find minimum in rotated sorted array solution

s = Solution()

assert s.findMin([5, 6, 7, 1, 2, 3, 4]) == 1
assert s.findMin([2, 3, 4, 5, 1]) == 1
assert s.findMin([1, 2, 3, 4, 5]) == 1
assert s.findMin([2, 1]) == 1
assert s.findMin([1, 2]) == 1
assert s.findMin([7]) == 7
assert s.findMin([-2, -1, -5, -4, -3]) == -5
assert s.findMin([0, 1, -3, -2, -1]) == -3
assert s.findMin([3, 4, 5, 6, 7, 8, 9, 1, 2]) == 1