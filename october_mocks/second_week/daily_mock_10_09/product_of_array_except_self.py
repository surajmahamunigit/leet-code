# 9

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Return the product of array except self.

        Args:
            nums (list[int]): integer array

        Returns:
            list[int]: product of array except self

        Time complexity: O(n) - n = len(nums)

        Space complexity: O(n)
        """

        result = [1] * len(nums)

        # pre numbers products
        pre = 1
        for index in range(len(nums)):
            result[index] = pre
            pre *= nums[index]

        # post numbers products
        post = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= post
            post *= nums[index]

        return result

# 9.07 -> 7 minutes to finish
# git commit -> feat: add product except self solution

s = Solution()
assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
assert s.productExceptSelf([2, 3]) == [3, 2]
assert s.productExceptSelf([0, 0]) == [0, 0]
assert s.productExceptSelf([0, 4]) == [4, 0]
assert s.productExceptSelf([1, 0]) == [0, 1]
assert s.productExceptSelf([5, 0, 2]) == [0, 10, 0]
assert s.productExceptSelf([-1, -1]) == [-1, -1]
assert s.productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]
assert s.productExceptSelf([2, -3, 4]) == [-12, 8, -6]
assert s.productExceptSelf([10, 0, 0, 3]) == [0, 0, 0, 0]
assert s.productExceptSelf([2] * 50) == [2 ** 49] * 50