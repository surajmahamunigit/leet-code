# 11.57

class Solution:
    def trapping_water(self, height: list[int]) -> int:
        """Find the maximum water trapped between the bars.

        Args:
            height (list[int]): list of integers representing each bars height

        Returns:
            int: total water trapped between the bars

        Time: O(n) - n = len(height)

        Space: O(1)
        """

        # height = [0,2,0,3,1,0,1,3,2,1]
        max_tap = 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left < right:

             if height[left] <= height[right]:
                 left_max = max(left_max, height[left])
                 water_trapped = (left_max - height[left])
                 max_tap += water_trapped
                 left += 1
             else:
                 right_max = max(right_max, height[right])
                 water_trapped = (right_max - height[right])
                 max_tap += water_trapped
                 right -= 1

        return max_tap

s = Solution()
print(s.trapping_water(height = [0,2,0,3,1,0,1,3,2,1]))
print(s.trapping_water(height = [7,8,9]))