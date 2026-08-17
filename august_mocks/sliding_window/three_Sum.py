# 10.58

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Find all the triplets that add up to zero.

        Args:
            nums: list of integers

        Returns:
            list of triplets that add up to zero

        Time: O(n^2) - n = len(nums)
        Space: O(1)
        """
        res = []
        nums.sort()

        for index in range(len(nums)):

            if index > 0 and nums[index] == nums[index - 1]:
                continue

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

# 11.46 -> 48 min with help to solve problem
# add it to imp list