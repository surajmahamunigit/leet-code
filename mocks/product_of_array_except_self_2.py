# algorithm
# take result array of same size res = [1] * len(nums)
# assume pre = 1, post =1
# first we will find out product of number that came before current num and then post numbers
# for every index in nums -> res[index] = pre, then modify pre for next num pre *= nums[index]
# # for every index in nums tracking backward -> res[index] *= post, then modify post for next num post *= nums[index]
# in end return result array

class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        """Find product of array except self.

        Args:
            nums: integer array

        Returns:
            integer array representing product of array

        Time: O(n) - n = len(nums)
        Space: O(n))
        """

        res = [1] * len(nums)

        # find pre multiplication
        pre = 1
        for index in range(len(nums)):
            res[index] = pre
            pre *= nums[index]          # for next num

        # find post multiplication
        post = 1
        for index in range(len(nums) - 1, -1, -1):
            res[index] *= post
            post *= nums[index]         # for next num


        return res

s = Solution()
#res = s.product_except_self(nums = [1,2,4,6])
res = s.product_except_self(nums = [-1,0,1,2,3])
print(res)