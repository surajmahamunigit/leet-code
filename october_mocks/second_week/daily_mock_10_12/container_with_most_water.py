# 10.50

# given -> integer array representing heigh of each line

# find -> max water contained

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """Find the maximum water hold by container.

        Args:
            height (list[int]): integer array representing height of each line

        Returns:
            int: maximum water contained between two lines and x axis

        Time complexity: O(n) - n = len(height)

        Space complexity: O(1)
        """

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(curr_area, max_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# 10.57 -> 7 minutes to finish problem
# git commit -> feat: add container with most water solution

s = Solution()
assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert s.maxArea([1, 1]) == 1
assert s.maxArea([4, 3, 2, 1, 4]) == 16
assert s.maxArea([1, 2, 1]) == 2
assert s.maxArea([1, 2, 4, 3]) == 4
assert s.maxArea([0, 2]) == 0
assert s.maxArea([0, 0, 0]) == 0
assert s.maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
assert s.maxArea([5, 5, 5, 5]) == 15
assert s.maxArea([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
assert s.maxArea([1] * 100000) == 99999
assert s.maxArea([9] + [0] * 99998 + [9]) == 899991
assert s.maxArea(list(range(1, 100001))) == 2500000000