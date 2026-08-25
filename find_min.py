# 8
# find minimum number in given rsa

# if val > nums[right] -> min belong on right side -> look here

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Find minimum number in given rotated sorted array.

        Args:
            nums: list of integers, rotated and sorted

        Returns:
            smallest number in nums

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:

            index = (left + right) // 2
            val = nums[index]

            # min on right or not
            if val > nums[right]:
                left = index + 1
            else:
                right = index

        return nums[left]

s = Solution()
assert s.findMin([3,4,5,1,2]) == 1
assert s.findMin([4,5,6,7,0,1,2]) == 0
assert s.findMin([11,13,15,17]) == 11
assert s.findMin([1]) == 1
assert s.findMin([2,1]) == 1
print("passed")


# 0.10 -> 10 min to solve