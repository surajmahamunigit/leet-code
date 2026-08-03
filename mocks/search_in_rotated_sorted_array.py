#   Algorithm:
# property of rotated sorted array is always one side of the
#   given nums = [4,5,6,7,0,1,2], target = 0, left = 0, right = len(nums)
#   while left <= right
#   mid = (left+right)//2,compare with nums[mid] with target, if equal return mid index
#   if nums[left] <= middle number -> left side is sorted and we look for target number in sorted side of array.
#   else right side of nums[mid] is sorted and we look for target in there.
#

# kind of hard to explain answer in words. already tried and spend too much time.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the index of the target number in given array or return -1.

        Args:
            nums: list of sorted rorted integers
            target: target number

        Returns:
            index of target number, else -1

        Time: O()
        Space: O()
        """

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left+right)//2
            mid_num = nums[mid]

            if mid_num == target:
                return mid

            # left side is sorted
            if nums[left] <= mid_num:

                if nums[left] <= target < mid_num:
                    right = mid - 1
                else:
                    left = mid + 1

            # right side is sorted
            else:
                if mid_num < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return - 1

s = Solution()
assert s.search([4,5,6,7,0,1,2], target = 0) == 4
print("passed")