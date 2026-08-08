class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the target number and return its index, else return -1.

        Args:
            nums: rotated sorted integer array
            target: integer number

        Returns:
            index of target number else -1

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

            # left of mid_num is sorted
            if nums[left] <= mid_num:
                if nums[left] <= target < mid_num:
                    right = mid_index - 1

                else:
                    left = mid_index + 1

            # right of mid_num is sorted
            else:
                if nums[mid_index] < target <= nums[right]:
                    left = mid_index + 1
                else:
                    right = mid_index - 1

        return - 1

s = Solution()
#res = s.search(nums = [3,4,5,6,1,2], target = 1)
res = s.search(nums = [3,5,6,0,1,2], target = 4)
print(res)

