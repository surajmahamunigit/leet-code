# 8.52

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        """Find all unique triplets that add up to zero.

        Args:
            nums (list[int]): list of integers

        Returns:
            list[list[int]]: list of triplets that add up to zero.

        Time: O(n^2) - n = len(nums)

        Space: O(1)
        """

        result = []
        nums.sort()

        # first number
        for index in range(len(nums)):

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # second and third number
            left = index + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[index] + nums[left] + nums[right]

                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[index], nums[left], nums[right]])

                    left += 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
        return result

s = Solution()
print(s.three_sum(nums = [-1,0,1,2,-1,-4]))
print(s.three_sum(nums = [0,1,1]))
print(s.three_sum(nums = [0,0,0]))