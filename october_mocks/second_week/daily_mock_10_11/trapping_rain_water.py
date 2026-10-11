# 2.29

# given height of each bar with width 1
# return how much rain water trapped

class Solution:
    def trap(self, height: list[int]) -> int:
        """Find the total water trapped between the bars.

        Args:
            height (list[int]): integer array representing height of each bar

        Returns:
            int: total water trapped between the bars

        Time complexity: O(n) - n = len(height)

        Space complexity: O(1)
        """

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water_trapped = 0

        while left < right:

            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
                right -= 1

        return water_trapped

# 2.38 -> 9 minutes to finish
# git commit -> feat: add total water trapped between bars solution

s = Solution()
assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert s.trap([4, 2, 0, 3, 2, 5]) == 9
assert s.trap([1]) == 0
assert s.trap([1, 2]) == 0
assert s.trap([2, 0, 2]) == 2
assert s.trap([3, 0, 0, 2, 0, 4]) == 10
assert s.trap([5, 4, 3, 2, 1]) == 0
assert s.trap([1, 2, 3, 4, 5]) == 0
assert s.trap([5, 0, 5]) == 5
assert s.trap([0, 0, 0]) == 0
assert s.trap([5, 2, 1, 2, 1, 5]) == 14
assert s.trap([4, 2, 3]) == 1
assert s.trap([2, 1, 0, 1, 3]) == 4
assert s.trap([7] + [0] * 100000 + [7]) == 700000
