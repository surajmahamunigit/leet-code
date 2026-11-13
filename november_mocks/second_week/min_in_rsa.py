# 8.32

class Solution:
    def find_minimum(self, nums: list[int]) -> int:
        """Find the minimum in a nonempty rotated sorted array of distinct integers.

        Args:
            nums: list of integers

        Returns:
            int: smallest number in the given list

        Time complexity: O(log n) - n = len(nums)

        Space complexity: O(1)
        """
        # [50, 60, 10, 20, 30]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid_index = (left + right) // 2

            if nums[mid_index] > nums[right]:
                left = mid_index + 1
            else:
                right = mid_index

        return nums[left]

s = Solution()

def check(values, expected):
    result = s.find_minimum(values)
    assert result == expected

check([4,5,6,1], 1)
check([1,2,3,4,5,6], 1)
check([1], 1)
check([-2,-1,0,4,5], -2)
print("all tests passed")