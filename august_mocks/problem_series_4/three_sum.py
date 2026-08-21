# 11
# given unsorted array and asked to find out unique pairs of triplets that add up to zero.
# fix first number then fix remaining two -> two pointers pattern problem

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Find all unique triplet pairs that add up to zero.

        Args:
            nums: list of unsorted array

        Returns:
            unique triples that add up to zer

        Time: O(n^2) - n = len(nums)
        Space: O(1)
        """
        res = []

        nums.sort()         # dont forget to sort the array. its find three number problem with unsorted array

        # fix first number
        for index, num in enumerate(nums):

            # skip on repetition
            if index > 0 and num == nums[index - 1]:
                continue

            # Fix two numbers
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

                    # skip on next repetition
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

# 11.12 -> 12 minute sto solve