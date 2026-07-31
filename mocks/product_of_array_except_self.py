# Algorithm:
# input array :nums= [1,2,3,4]. create same size output array for product of array. lets assume its called answer.
# assume pre = 1, and use it to calculate product of nums in array that came before nums[i].
# for every nums[i] in array stating from i = 0, result[i] = pre amd pre = pre * nums[i] for  nums[i+1]
# this way we calculated multiplication of nums that came before each num. now calculate, post number multiplication.
# assume post = 1, we traverse the array backward from len(nums) - 1 to 0. each result[i] = post * result[i] and post = post * nums[i]
# after for loop is over we will get product of array.



# example: nums= [1,2,3,4]
# result = [1, 1, 1, 1], pre = 1
# i = 0 -> result[0] = 1, pre = 1
# i = 1 -> result[1] = 1, pre = 2
# i = 2 -> result[2] = 2, pre = 6
# i = 3 -> result[3] = 6, pre = 24 (gets ignored)
# result = [1, 1, 2, 6]
# post = 1
# i = 3 -> result[3] = 6, post = 4
# i = 2 -> result[2] = 8, post = 12
# i = 1 -> result[1] = 12, post = 24
# i = 0 -> result[0] = 24, post = 24

class Solution:
    def productExceptself(self, nums: list[int]) -> list[int]:
        """Find product of array except itself.

        Args:
            nums : given int array

        Returns:
            int array containing product of each number in array except self.

        Time: O(n) - n = len(nums)
        Space: O(1)
        """

        result = [1] * len(nums)        # output same size as input

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
assert s.productExceptself([1,2,3,4]) == [24, 12, 8, 6]
assert s.productExceptself([-1,1,0,-3,3]) == [0,0,9,0,0]
print("passed")