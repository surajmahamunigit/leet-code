class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Args:
             nums: List of integers

        Returns:
            list[int] : list of product of nums except self

        Time: O(n)
        Space: O(1)
        """
        res = [1] * len(nums)

        # Pre-product : product of nums on left side
        # rule: Store pre first then change it next num
        pre = 1
        for i in range(len(nums)):
            res[i] = pre            # store pre
            pre = pre * nums[i]     # change pre

        # Find product of nums on right side and output
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post          # multiply with post and then store post
            post = post * nums[i]   # change post

        return res

result = Solution().productExceptSelf(nums=[1, 2, 3, 4])
print(result)