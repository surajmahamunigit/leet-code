# 6.58

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Find product of array with except itself.

        Args:
            nums: integer array

        Returns:
            result array where result[i] is product of all numbers in array except nums[i]

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

s = Solution()
assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
assert s.productExceptSelf([1]) == [1]
assert s.productExceptSelf([]) == []
print("passed")

# 7.04 -> 6 min to finish