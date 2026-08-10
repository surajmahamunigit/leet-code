# algorithm
# given nums array and its binary search, array is sorted, and find target numbers index if found, else return -1
# while left <= right -> left = 0, right = len(nums) - 1
# find mid index -> then mid number -> if mid number == target -> returns its index
# if target greater than mid number -> left = mid index + 1
# else right = mid index - 1
# in end return -1

class Solution:
    def binary_search(self, nums: list[int], target: int) -> int:
        """Find and return the index of target num.

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
            mid_index = (left + right) // 2
            mid_num = nums[mid_index]

            if target == mid_num:
                return mid_index
            elif target > mid_num:
                left = mid_index + 1
            else:
                right = mid_index - 1

        return - 1

s = Solution()
#res = s.binary_search(nums = [-1,0,2,4,6,8], target = 3)
res = s.binary_search(nums = [-1,0,2,4,6,8], target = 4)
print(res)