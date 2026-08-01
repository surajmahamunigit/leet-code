# algorithm:
# given nums = [1,0,1,2,-1,-4]
# sort the given array -> nums = [-4, -1, 0, 1, 1, 2]
# we will use three pointers to solve the problem. index, left and right
# first we start tracing from index = 0 till len(nums)-1
# index = 0, left = index + 1, right = len(nums) - 1
# if index > 0 and nums[i] and nums[i-1] are equal-> skip the nums[]
# index = 0, left = 1, right = 5 ->
# while left < right -> count the total -> if total < 0, increase left by 1, if target  > 0, decrease right index by 1. if total == 0, result.append([nums[index], nums[left], nums[right])
# in end return result

# example :
# nums = [1,0,1,2,-1,-4]
# sort -> [-4, -1, 0, 1, 1, 2]
# for index in range(len(nums)) -> nums [0] = -4, left = 1, nums[1] = -1, right = 5, nums[5] = 2 -> left < right-> total = -3 < 0 -> move left forward
# nums [0] = -4, left = 2, nums[2] = 0, right = 5, nums[5] = 2 -> left < right -> total = -2 < 0 -> move left forward
# nums [0] = -4, left = 3, nums[3] = 1, right = 5, nums[5] = 2 -> left < right -> total = -1 < 0 -> move left forward
# nums [0] = -4, left = 4, nums[4] = 1, right = 5, nums[5] = 2 -> left < right -> total = -3 < 0 -> move left forward -> left=right=5 -> left < right -> False
# nums [1] = -1, left = 2, nums[2] = 0, right = 5, nums[5] = 2 -> left < right -> total = 1 > 0 -> move right inward
# nums [1] = -1, left = 2, nums[2] = 0, right = 4, nums[4] = 1 -> left < right -> total = 0 -> [-1, 0, 1] -> move left forward
# nums [1] = -1, left = 3, nums[3] = 1, right = 4, nums[4] = 1 -> left < right -> total = 1 > 0 -> move right inward
# nums [1] = -1, left = 3, nums[3] = 1, right = 3, nums[3] = 1 -> left < right -> False
# nums [2] = 0, left = 3, nums[3] = 1, right = 5, nums[5] = 2 -> left < right -> total = 3 > 0  -> move right inward
# nums [2] = 0, left = 3, nums[3] = 1, right = 4, nums[4] = 1 -> left < right -> total = 2 > 0  -> move right inward -> left = right = 3 -> left < right -> False
# nums [3] = 1, left = 4, nums[4] = 1, right = 5, nums[5] = 2 -> left < right -> total = 4 > 0  -> move right inward -> left = right = 4 -> left < right -> False

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Find all possible triplets that add up to zero from given array.

        Args:
            nums: list of integers

        Returns:
            list of triplets that add up to zero.

        Time: O(n^2) - n = len(nums)
        Space: O(n) - sorted array
        """

        result = []
        sorted_nums = sorted(nums)

        for index in range(len(sorted_nums)):

            # skip first numbers repetition
            if index > 0 and sorted_nums[index] == sorted_nums[index - 1]:
                continue

            left = index + 1
            right = len(sorted_nums) - 1
            while left < right:

                total = sorted_nums[index] + sorted_nums[left] + sorted_nums[right]

                # two-pointer solution
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([sorted_nums[index], sorted_nums[left], sorted_nums[right]])

                    # found solution. now move left
                    left += 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1       # to skip the inner numbers repetition

        return result

s = Solution()
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1,-1,2],[-1,0,1]]
assert s.threeSum([0,1,1]) == []
print("passed")
