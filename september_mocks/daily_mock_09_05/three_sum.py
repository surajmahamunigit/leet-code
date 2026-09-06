# 6.15

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Find all the unique triplets that add up to zero.

        Args:
            nums (list[int]): list of integers

        Returns:
            lis[list[int]]: list of all unique triplet pairs that add up to zero

        Time: O(n^2) - n = len(nums)
        Space: O(1)
        """

        result = []
        nums.sort()

        # fix the first number
        for index in range(len(nums)):

            # skip duplicate
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # fix remaining two numbers
            left = index + 1
            right = len(nums) - 1

            while left < right:

                curr_sum = nums[index] + nums[left] + nums[right]

                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    result.append([nums[index], nums[left], nums[right]])

                    left += 1
                    # skip duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result

s = Solution()
def normalize(result):
    return sorted(sorted(triplet) for triplet in result)

assert normalize(s.threeSum([-1,0,1,2,-1,-4])) == normalize([[-1,-1,2],[-1,0,1]])
assert s.threeSum([0,1,1]) == []
assert s.threeSum([0,0,0]) == [[0,0,0]]
assert s.threeSum([-2,0,0,0,2,2])  # check yourself for duplicate triplets
assert s.threeSum([]) == []
assert s.threeSum([0]) == []

print('passed')

