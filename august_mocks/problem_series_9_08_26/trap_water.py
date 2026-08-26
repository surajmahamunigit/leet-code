# 12.02
#given elevation map and asked to find how much water is trapped between bars

class Solution:
    def trapWater(self, height: list[int]) -> int:
        """Find trapped water between bars.

        Args:
            height: integer array representing bar height

        Returns:
            total water trapped between bars

        Time: O(n) - n = len(height)
        Space: O(1)
        """
        total_water = 0
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        while left < right:

            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water_trapped = left_max - height[left]
                total_water += water_trapped
                left += 1
            else:
                right_max = max(right_max, height[right])
                water_trapped = right_max - height[right]
                total_water += water_trapped
                right -= 1

        return total_water

s = Solution()
res = s.trapWater([0,2,0,3,1,0,1,3,2,1])
print(res)

# 12.15 -> 13 min to solve