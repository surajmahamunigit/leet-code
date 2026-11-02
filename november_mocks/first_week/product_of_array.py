# 7.49

class Solution:
    def product_excect_self(self, nums: list[int]) -> list[int]:
        """Find the product of array except self.

        Args:
            nums (list[int]): integer array

        Returns:
            list[int]: product of array except self

        Time complexity: O(n) - len(nums)

        Space complexity: O(1)
        """

        # find product of pre numbers
        pre = 1
        result = [1] * len(nums)
        for index in range(len(nums)):
            result[index] = pre
            pre *= nums[index]

        # find product with post numbers
        post = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= post
            post *= nums[index]

        return result

s = Solution()

def check(values, expected):
    result = s.product_excect_self(values)
    assert result == expected

check([1,2,3,4], [24, 12, 8, 6])
check([1,2,4,6], [48,24,12,8])
check([-1,0,1,2,3], [0, -6,0,0, 0])
check([1,2], [2,1])
check([0,2,0,4], [0,0,0,0])
print("all tests passed")

# 7.59 -> 10 minute sto solve the problem
# git commit -> feat: add product of array except self solution