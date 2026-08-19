# 10.27
# given integer array, asked to find out pre and post number multiplication for each number

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Find product of an array except self.

        Args:
            nums: integer array

        Returns:
            product of array except self

        Time: O(n) - n = len(nums)
        Space: O(1) auxiliary
        """

        res = [1] * len(nums)

        # pre number multiplication
        pre = 1
        for index in range(len(nums)):
            res[index] = pre
            pre *= nums[index]

        # post number multiplication
        post = 1
        for index in range(len(nums) - 1, -1, -1):
            res[index] *= post
            post *= nums[index]

        return res

s = Solution()
assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
assert s.productExceptSelf([1]) == [1]
assert s.productExceptSelf([]) == []
print("passed")

# 10.32 -> 5 min to solve