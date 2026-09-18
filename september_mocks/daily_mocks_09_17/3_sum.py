# 6.17

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Find the pairs of three numbers that add up to zero.

        Args:
            nums (list[int]): given integer array

        Returns:
            list[list[int]]: pairs of three numbers that add up to zero.

        Time: O(n^2) - n = len(nums)

        Space: O(n)
        """
        result = []

        # sort the given array
        nums.sort()

        # fix the first number
        for index in range(len(nums)):

            # skip first duplicate
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # fix next two numbers
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

                    # move left forward and skip on duplicate
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result

s = Solution()
print(s.threeSum(nums = [0, 1, 1]))

# 6.26 -> 9 min