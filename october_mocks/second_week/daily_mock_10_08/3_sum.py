# 11.02

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Find all the unique triplet pairs that add up to zero.

        Args:
            nums (list[int]): given integer array

        Returns:
            list[list[int]]: returns all the unique triplets that add up to zero

        Time complexity: O(n^2) - n = len(nums)

        Space complexity: O(1)
        """
        result = []

        nums.sort()
        # fix the first number
        for index in range(len(nums)):

            # avoid duplicate
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # find remaining two numbers
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
                    # avoid duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result

# 11.11 -> 9 minute sto solve problem
# git commit -> feat: add 3 sum solution

s = Solution()
def norm(r): return sorted(map(sorted, r))
assert norm(s.threeSum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
assert norm(s.threeSum([0, 1, 1])) == []
assert norm(s.threeSum([0, 0, 0])) == [[0, 0, 0]]
assert norm(s.threeSum([0, 0, 0, 0])) == [[0, 0, 0]]
assert norm(s.threeSum([-2, 0, 1, 1, 2])) == [[-2, 0, 2], [-2, 1, 1]]
assert norm(s.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])) == [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
assert norm(s.threeSum([1, 2, -2, -1])) == []
assert norm(s.threeSum([3, 0, -2, -1, 1, 2])) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
assert norm(s.threeSum([0] * 3000)) == [[0, 0, 0]]