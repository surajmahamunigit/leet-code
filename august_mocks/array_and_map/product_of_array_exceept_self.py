# 1.33

class Solution:
    def product_of_array(self, nums: list[int]) -> list[int]:
        """Find product of array except self.

        Args:
            nums: integer array

        Returns:
            product array where result[i] is product of all numbers except nums[i]

        Time: O(n) - n = len(nums)
        Space: O(n)
        """

        res = [1] * len(nums)

        # calculate pre number product
        pre = 1
        for index in range(len(nums)):
            res[index] = pre
            pre *= nums[index]

        # post number calculation
        post = 1
        for index in range(len(nums) - 1, -1, -1):
            res[index] *= post
            post *= nums[index]

        return res

s = Solution()
res = s.product_of_array(nums = [-1,0,1,2,3])
print(res)