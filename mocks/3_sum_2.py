# algorithm
# given unsorted scending array, we have to find three numbers that upto zero
# first
# first we fix one number then use two pointer solution to find the answer
# for every index in given nums
# if nums[index] and nums[index - 1] is same then continue -> no duplicate pairs
# left = index + 1, right = len(nums) - 1, while left < right
# if curr_sum == target -> return [index, left, right]
# if target < curr_sum -> right inward, else move left forward
# in end return []


class Solution:
    def three_sum(self, nums: list[int]) -> list[int]:
        """Return indices of three numbers that add upto zero.

        Args:
            nums: unsorted integer array

        Returns:
              list of three number that add upto zero

        Time: O(n^2) - n = len(nums) - outer loop and inside while loop
        Space:
        """
        result = []

        # given array is unsorted, we need sorted array to use two-pointer solution
        nums.sort()

        for index in range(len(nums)):

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[index] + nums[left] + nums[right]

                if curr_sum == 0:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    left += 1

        return result

s = Solution()
#res = s.three_sum(nums = [-1,0,1,2,-1,-4])
res = s.three_sum(nums = [0,1,1])
print(res)