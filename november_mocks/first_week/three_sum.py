# 12.51

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        """Find all the unique pairs of three numbers that add up to zero.

        Args:
            nums (list[int]): integer array

        Returns:
            list[list[int]]: list of unique triplets that add pto zero.

        Time complexity: O(n^2) - n = len(nums)

        Space complexity: O(n) - for sorting
        """

        # nums = [-1,0,1,2,-1,-4]

        result = []
        nums.sort()

        # first the first number
        for index in range(len(nums)):
            # skip the duplicate
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

                    left += 1
                    # skip duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result

s = Solution()

def check(values, expected):
    result = s.three_sum(values)
    normalize = lambda groups : sorted(sorted(g) for g in groups)
    assert normalize(result) == normalize(expected)

check([-1,-2,0,1,2,], [[-1,0,1], [-2,0,2]])
check([0,0,0], [[0,0,0]])
check([-1,0,1,2,-1,-4], [[-1,0,1], [-1,2,-1]])
check([0,1,1], [])
check([0,0,0,0], [[0,0,0]])
check([-2,-2,0,0,2,2], [[-2,0,2]])
print("all passed")