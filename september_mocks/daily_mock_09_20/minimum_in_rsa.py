# 6.54

class Solution:
    def find_minimum(self, nums: list[int]) -> int:
        """Find the smallest number in given rsa.

        Args:
            nums (list[int]): list of integers

        Returns:
            int: smallest number

        Time: O(log n) - n = len(nums)

        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            num = nums[mid]

            if num >= nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

s = Solution()
print(s.find_minimum(nums = [3,4,5,6,1,2]))
print(s.find_minimum(nums = [4,5,0,1,2,3]))
print(s.find_minimum(nums = [3,4,5,6]))

# 7.01 -> 7 min