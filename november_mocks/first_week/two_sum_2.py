# 11.45

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """Find the 1-indexed indices of two numbers from given array that add upto target.

        Args:
            nums (list[int]): integer array sorted in ascending order
            target (int): target addition

        Returns:
            list[int]: 1-indexed positions of two numbers that add up to target

        Time complexity: O(n) - n = len(nums)

        Space complexity: O(1)
        """

        # nums = [1,2,3,4], target = 5

        left = 0
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum == target:
                return [left + 1, right + 1]

            if curr_sum < target:
                left += 1
            else:
                right -= 1

        return []

s = Solution()

def check(values, target, expected):
    result = s.two_sum(values, target)
    assert result == expected

check([-1,0,1], 0, [1,3])
check([0,0], 0, [1,2])
check([-3,-2,3,4], 2, [2,4])
check([1,2,3,4,5,6,7], 3, [1,2] )
check([-3,-2,-1,2], -3, [2,3])
print("all tests passed")

# 11.57 -> 12 minute sto solve and write test cases
# git commit -> feat: add two sum 2 solution