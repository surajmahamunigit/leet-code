# 11.28
# given integer array and asked to find all triplets that add up to zero

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Find all the triplets that add up to zero.

        Args:
            nums: integer array

        Returns:
            list of all triplets that add up to zero.

        Time: O(n^2) - n = len(nums)
        Space: O(1)
        """
        res = []
        nums.sort()

        # Fix first number
        for index in range(len(nums)):

            # skip on duplicate
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # two pointers pattern
            left = index + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[index] + nums[left] + nums[right]

                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    res.append([nums[index], nums[left], nums[right]])

                    # move left
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res

s = Solution()
res = s.threeSum([-1,0,1,2,-1,-4])
print(res)

# 11.38 -> 10 min to solve