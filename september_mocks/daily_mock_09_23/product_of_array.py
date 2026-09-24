# 6.08

class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        """Find product of array except self.

        Args:
            nums (list[int]): list of integers

        Returns:
            list[int]: product of array except self

        Time: O(n) - n = len(nums)

        Space: O(n)
        """
        result = [1] * len(nums)

        # find the product with pre numbers
        pre = 1
        for index in range(len(nums)):
            result[index] = pre
            pre *= nums[index]

        # find product with post numbers
        post = 1
        for index in range(len(nums)-1, -1, -1):
            result[index] *= post
            post *= nums[index]

        return result

s = Solution()
print(s.product_except_self([1,2,4, 6]))
print(s.product_except_self(nums = [-1,0,1,2,3]))