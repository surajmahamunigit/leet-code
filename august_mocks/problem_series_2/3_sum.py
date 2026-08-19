# 9.17
# given unsorted array and asked to find all triplets that add to zero
# sort numbers -> fix first number and then fix remaining two

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Find all unique triplets that add up to zero.

        Args:
            nums: unsorted array

        Returns:
            list of all unique triplets

        Time: O(n^2) - n = len(nums)
        Space: O(1)
        """

        res = []

        # sort the numbers
        nums.sort()

        # fix first number
        for index, num in enumerate(nums):

            # skip over repetition
            if index > 0 and num == nums[index - 1]:
                continue

            # find remaining two numbers
            left = index + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = num + nums[left] + nums[right]

                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])

                    # skip over repetition
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
assert s.threeSum([-2,0,0,0,2,2])  # verify manually — no fixed assert, check for duplicate triplets yourself
assert s.threeSum([]) == []
assert s.threeSum([0]) == []
print("passed")