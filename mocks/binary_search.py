# algorithm
# given sorted array with unique integers
# assume left = 0 and right = len(nums) - 1
# while left <= right:
# mid = (left+right)//2, mid_num = nums[mid] -> if mid_num==target, return index mid, -> if target > mid_num => left = mid+1, else right=mid-1
# in end return -1, in case target not found

# example:
# nums = [-1,0,3,5,9,12], target = 9, left = 0, right= 5
# 0 <= 5 -> mid = 2, mid_num = 3 not equal to target, target > 3 -> left = 3
# 3 <= 5 -> mid = 4, mid_num = 9 equal to target, -> return index=4

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the target number in given sorted array.

        Args:
            nums: sorted integer array
            target: target integer

        Returns:
            index of target number if found, else -1

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left+right)//2
            mid_num = nums[mid]

            if mid_num == target:
                return mid
            elif mid_num < target:
                left = mid + 1
            else:
                right = mid - 1

        return - 1

s = Solution()
assert s.search(nums = [-1,0,3,5,9,12], target = 9) == 4
assert s.search(nums = [-1,0,3,5,9,12], target = 2) == -1
assert s.search(nums = [-1,0,3,5,9,12], target = 22) == -1
assert s.search(nums = [-1,0,3,5,9,12], target = -2) == -1
assert s.search(nums = [-1,], target = -1) == 0
assert s.search(nums = [-1,], target = 1) == -1

print("passed")