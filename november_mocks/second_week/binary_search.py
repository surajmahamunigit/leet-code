# 4.38

class Solution:
    def binary_search(self, nums: list[int], target: int) -> int:
        """Find the target element in given ascending array using binary search.

        Args:
            nums: list of integers in ascending order
            target: target number to look for

        Returns:
            int: index of the target number if found, else -1

        Time complexity: O(log n) - n = len(s)

        Space complexity: O(1)
        """

        # [10,20,30 40, 40, 50], target = 20

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2

            if nums[mid_index] > target:
                right = mid_index - 1
            elif nums[mid_index] < target:
                left = mid_index + 1
            else:
                return mid_index

        return -1

s = Solution()

def check(values, target, expected):
    result = s.binary_search(values, target)
    assert result == expected

check([-2,-1,0,2,5,6], 1, -1)
check([10,60,80,90], 90, 3)
check([10,20,30,40], 50, -1)
check([0,0,0], 0, 1)
print("all tests passed")