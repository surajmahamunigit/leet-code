# 4.07
# given integer array and asked to find product of it with pre and post numbers
# array patter

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Find product of an array except itself.

        Args:
            nums: list of integers

        Returns:
            res array where res[i] is product of all numbers in nums except at nums[i]

        Time: O(n) - n = len(nums)
        Space: O(n)
        """
        res = [1] * len(nums)

        pre = 1
        for index in range(len(nums)):
            res[index] = pre
            pre *= nums[index]

        post = 1
        for index in range(len(nums) - 1, -1, -1):
            res[index] *= post
            post *= nums[index]

        return res

# 4.14 -> 7 min to solve