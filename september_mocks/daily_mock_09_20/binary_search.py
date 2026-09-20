# 3.20

class Solution:
    def binary_search(self, nums: list[int], target: int) -> int:
        """Find the target number using binary search and return its index.

         Args:
             nums (list[int]): sorted integer array
             target (int): number to look for

         Returns:
             int: index of target number

         Time: O(log n) - n = len(nums)

         Space: O(1)
         """
        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (left + right) // 2
            curr_num = nums[index]

            if curr_num < target:
                left = index + 1
            elif curr_num > target:
                right = index - 1
            else:
                return index

        return - 1

s = Solution()
print(s.binary_search(nums = [-1,0,2,4,6,8], target = 4))
print(s.binary_search(nums = [-1,0,2,4,6,8], target = 3))

# 3.27 -> 7 min