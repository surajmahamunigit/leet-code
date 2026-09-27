# 1.27

class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        """Find product of array except self.

        Args:
            nums (list[int]): list of integers

        Returns:
            list[int]: product array

        Time: O(n) - len(nums)

        Space: O(n)
        """

        # nums = [1,2,4,6]

        result = [1] * len(nums)
        pre = 1
        for index in range(len(nums)):
            result[index] = pre
            pre *= nums[index]

        post = 1
        for index in range(len(nums) - 1, - 1, -1):
            result[index] *= post
            post *= nums[index]

        return result

s = Solution()
print(s.product_except_self([1,2,3,4,5]))
print(s.product_except_self([1,2]))
print(s.product_except_self(nums = [-1,0,1,2,3]))