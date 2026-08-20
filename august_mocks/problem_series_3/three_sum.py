# 9.38
# given unsorted array, asked to find triplets that add up to zero.
# sort array -> fix first number -> use sliding window to find remaining two


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Find all triplet that add up to zero.

        Args:
            nums: unsorted array

        Returns:
            list of pairs of triplets that add up to zero

        Time: O(n^2) - n = len(nums)
        Space: O(1)
        """

        res = []

        # sort the array
        nums.sort()

        # fix first number
        for index, num in enumerate(nums):

            # skip of repetition
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
                    res.append([num, nums[left], nums[right]])

                    # move left for next possibility
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res

s = Solution()
def normalize(result):
    return sorted(sorted(triplet) for triplet in result)

assert normalize(s.threeSum([-1,0,1,2,-1,-4])) == normalize([[-1,-1,2],[-1,0,1]])
assert s.threeSum([0,1,1]) == []
assert s.threeSum([0,0,0]) == [[0,0,0]]
assert s.threeSum([]) == []
assert s.threeSum([0]) == []
print("passed")

# 9.50 -> 12 min to solve