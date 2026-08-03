# algorithm:
# nums = [1,2,3,4]
# assume result = [1] * len(nums) and pre = 1
# we will first calculate product of previous number for each number and store it in result array at respective index of number
# for each number in array -> result[i] = pre, then calculate pre for next number, pre *= nums[i], for last num pre will be ignored
# post = 1, we will calculate product of previous numbers and post number for each number and store it in result array at respective index of number
# in this case we start from end of array, for each num, result[i] *= post, then post *= nums[i] for next number. last one will be ignored again.
# return result

# nums = [1,2,3,4], result = [1,1,1,1], pre = 1
# for i = 0, result = [1,1,1,1]
# for i = 1, result = [1,1,1,1]
# for i = 2, result = [1,1,2,1]
# for i = 3, result = [1,1,2,6]

# nums = [1,2,3,4], result = [1,1,2,6], post = 1
# for i = 3,  result = [1,1,2,6], post = 4
# for i = 2,  result = [1,1,8,6], post = 12
# for i = 1,  result = [1,12,8,6], post = 24
# for i = 0,  result = [24,12,8,6], post = 4
# result = [24,12,8,6]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Find product of an array except itself.

        Args:
            nums: given integer array

        Returns:
            array containing, product of each number except itself.

        Time: O(n) - n = len(nums)
        Space: O(1)
        """

        result = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result

s = Solution()
assert s.productExceptSelf([1]) == [1]
assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
assert s.productExceptSelf([]) == []
print("passed")