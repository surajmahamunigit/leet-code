# 9.09

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the target number in given rotated sorted array and return its index.

        Args:
            nums: given nonempty rotated sorted integer array
            target: integer to look for

        Returns:
             int: 0-indexed target number index if found, else -1

        Time complexity: O(log n) - n = len(nums)

        Space complexity: O(1)
        """

        # nums = [4,5,6,1,2,3], target = 2

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2

            if nums[mid_index] == target:
                return mid_index

            # left side is sorted
            if nums[left] <= nums[mid_index]:
                if nums[left] <= target < nums[mid_index]:
                    right = mid_index - 1
                else:
                    left = mid_index + 1
            # right side is sorted
            else:
                if nums[mid_index] < target <= nums[right]:
                    left = mid_index + 1
                else:
                    right = mid_index - 1
        return - 1

s = Solution()

def check(values, target, expected):
    result = s.search(values, target)
    assert result == expected

check([], 1, -1)
check([1], 1, 0)
check([1], 2, -1)
check([1,2,3], 2, 1)
check([2,3,1], 1, 2)
check([4,5,6,1,2], 5, 1)
check([-2,-1,0,2,3,4],3, 4)
print("all tests passed")
