# 8.29

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """Find two numbers that add upto target and return their indices.

        Args:
            nums (List[int]): list of integers
            target: integer

        Returns:
            list[int]: indices of two numbers that add up to target and return them.

        Time complexity: O(n) - n = len(nums)

        Space complexity: O(n)
        """

        seen = {}
        for index in range(len(nums)):
            complement = target - nums[index]

            if complement in seen:
                return [seen[complement], index]

            seen[nums[index]] = index

        return []

s = Solution()

def check(values, target, expected):
    result = s.two_sum(values, target)
    assert result == expected

check([3,4,5,6], 7, [0,1])
check([1,2],3, [0,1])
check([-1,2,4,5,6], 3, [0,2])
check([-1,0,1], 0, [0,2])
print("all passed")

# 8.38 -> 9 minutes to solve and write test cases
# git commit -> feat: add two sum solution