# 12.39
# given integer array and asked to return product of array except self.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Find product of array except self.

        Args:
            nums: integer array

        Returns:
            product of array except self

        Time: O(n) - n = len(nums)
        Space: O(1)
        """
        result = [1] * len(nums)

        # calculate multiplication with previous numbers
        pre = 1
        for index in range(len(nums)):
            result[index] = pre
            pre *= nums[index]

        # calculate multiplication with post numbers
        post = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= post
            post *= nums[index]

        return result

s = Solution()
assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
assert s.productExceptSelf([1]) == [1]
assert s.productExceptSelf([]) == []
print("passed")

# 12.44 -> 5 min to solve