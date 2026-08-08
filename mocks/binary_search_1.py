# algorithm
# binary search -> sorted array
# left = 0, right = len(nums)
# execute loop while left <= right
# if mid = target , return mid_index
# else mid < target -> left = mid index + 1
# else mid > target -> right = mid_index - 1

class Solution:
    def binary_search(self, nums: list[int], target: int) -> int:
        """Find the target number and return its index else return -1

        Args:
            nums: sorted integer array
            target: integer number

        Returns:
            index of target if found, else returns - 1

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2
            mid_num = nums[mid_index]

            if mid_num == target:
                return mid_index
            elif mid_num < target:
                left = mid_index + 1
            else:
                right = mid_index - 1

        return -1

s = Solution()
res = s.binary_search(nums = [-1,0,2,4,6,8], target = 3)
print(res)