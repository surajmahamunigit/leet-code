# 12.40

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Find all the triplets that add up to zero.

        Args:
            nums: integer array

        Returns:
            list of all triplets that add up to zero

        Time: O(n^2) - n = len(nums)
        Space: O(1)
        """
        res = []

        # Using pointer strategy
        nums.sort()

        # fix first pointer
        for index, num in enumerate(nums):

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # fix two pointers
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

# 12.51 -> 11 min to solve
# keep this problem in daily problem solving list for next 4 days, if you can remember for me.