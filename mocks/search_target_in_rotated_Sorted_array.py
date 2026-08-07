# algorithm
# given rotated sorted array and find target num
# assum left = 0, right = len(nums) - 1
# mid_index = (left + right) // 2, mid_num = nums[mid_index]
# now we look for target in sorted side of the rotated sorted array
# if nums[left] <= mid_num -> left side of mid_num is sorted -> if target num > mid_num, left = mid_index + 1, else right = mid_index
# else right side of mid_num is sorted and we look into it same way


class Solution:
    def search_in_rotated_sorted_array(self, nums: list[int], target: int) -> int:
        """"Find and return the index of target number in nums array.

        Args:
            nums: integer rotated sorted array
            target: target integer number

        Returns:
              index of target number  else -1

        Time:
        Space:
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2
            mid_num = nums[mid_index]

            if mid_num == target:
                return mid_index

            # if left side of mid_num is sorted
            if nums[left] <= mid_num:

                if mid_num < target or target < nums[left]:
                    left = mid_index + 1
                else:
                    right = mid_index - 1

            # maybe right side of mid_num is sorted
            else:
                if target < mid_num or target > nums[right]:
                    right = mid_index - 1
                else:
                    left = mid_index + 1
        return - 1

s = Solution()
res = s.search_in_rotated_sorted_array(nums = [3,4,5,6,1,2], target = 1)
print(res)

