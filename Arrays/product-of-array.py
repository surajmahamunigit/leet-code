"""
Given an integer array nums, return an array output
where output[i] is the product of all the elements
of nums except nums[i].
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:


        # [1,1,1,1,1]
        result = [1] * len(nums)

        pre = 1

        for i in range(len(nums)):

            result[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result

result = Solution().productExceptSelf(nums=[1,2,3,4,5])
print(result)