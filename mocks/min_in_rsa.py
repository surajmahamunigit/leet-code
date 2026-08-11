# algorithm
# given nums = [3,4,5,6,1,2] rotated sorted array -> doesnt matter binary search is done search is only sorted part, whole array doesnt has tio be sorted
# left = 0, right = len(nums) - 1
# find mid_index then mid_bum -> if mid_num > nums[right] -> min belongs to right of mid_num -> left = mid_index + 1
# else right = mid_index

class Solution:
    def min_in_rsa(self, nums: list[int]) -> int:
        """Find minimum number in given RSA.

        Args:
            nums: integer RSA

        Returns:
            minimum number in RSA

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid_index = (left + right) // 2
            mid_num = nums[mid_index]

            if mid_num > nums[right]:
                left = mid_index + 1
            else:
                right = mid_index

        return nums[right]

s = Solution()
#res = s.min_in_rsa(nums = [3,4,5,6,1,2])
#res = s.min_in_rsa(nums=[1,2,3,4,5])
res = s.min_in_rsa(nums = [4,5,0,1,2,3])
print(res)
