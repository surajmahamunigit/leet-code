# algorithm
# given nums = [3,4,5,6,1,2], target = 1, rotated sorted array and target is given
# left = 0, right = len(nums) - 1
# while left <= right
# mid_index = (left + right) // 2, mid_num = nums[mid_index]
# if mid_num == target, return mid_index
# if nums[left] <= target < mid_num -> right = mid_index - 1, else left = mid_index + 1
# if mid_num < target <= nums[right] -> left = mid_index + 1, else right = mid_index - 1

class Solution:
    def search_in_res(self, nums: list[int], target: int) -> int:
        """Find and return the index of target number in nums else -1.

        Args:
            target: target number
            nums: list of rotated sorted integers

        Returns:
            index of target number in nums

        Time: O(log n)- n = len(nums)
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_num = nums[mid_index]

            if target == mid_num:
                return mid_index

            # left side is sorted
            if nums[left] <= mid_num:
                if nums[left] <= target < mid_num:
                    right = mid_index - 1
                else:
                    left = mid_index + 1
            else:
                if mid_num < target <= nums[right]:
                    left = mid_index + 1
                else:
                    right = mid_index - 1

        return - 1

s = Solution()
#res = s.search_in_res(nums = [3,4,5,6,1,2], target = 1)
#res = s.search_in_res(nums = [3,5,6,0,1,2], target = 4)
res = s.search_in_res([1,2,3,4,5,6,7,8,9], 9)
print(res)

