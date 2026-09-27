# 1.54

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        """Find all the unique triplets that add up to zero.

        Args:
            nums (list[int]): list of integers

        Returns:
            lis[list[int]]: list of all unique triplets that dd up to zero

        Time: O(n^2) - n = len(nums)

        Space: O(1)
        """

        nums.sort()

        result = []

        # find first number
        for index, num in enumerate(nums):

            # skip on duplicate
            if index > 0 and num == nums[index - 1]:
                continue

            # fix next two numbers
            left = index + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = num + nums[left] + nums[right]

                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])

                    left += 1
                    # skip on duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result

s = Solution()
print(s.three_sum([-1, 0, 1, 2, -1, -4]))
print(s.three_sum([0, 0, 0, -1, 1, 0]))