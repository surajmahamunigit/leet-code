# 7.59

class Solution:
    def max_area(self, height: list[int]) -> int:
        """Find the maximum water container can hold.

        Args:
            height (list[int]): integer array representing height of each bar

        Returns:
            int: maximum water container can store

        Time complexity: O(n) - n = len(height)

        Space complexity: O(1)
        """

        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

s = Solution()

def check(values, expected):
    result = s.max_area(values)
    assert result == expected

check([1, 1], 1)
check([0,1], 0)
check([1,2,3], 2)
check([3,2,1], 2)
check([0,0,0], 0)
check([2,2,2], 4)
check([1,7,2,5,4,7,3,6], 36)
print("all tests passed")

# 8.13 -> 14 minutes to solve the problem

# git commit -> feat: add container with most water solution
