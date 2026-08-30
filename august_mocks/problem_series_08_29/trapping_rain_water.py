# 3.32


class Solution:
    def trap(self, height: list[int]) -> int:
        """Find the water trapped between the bars.

        Args:
             height: integer array representing height of each bar

        Returns:
            total water trapped in bars

        Time: O(n) - n = len(height)
        Space: O(1)
        """
        water_trapped = 0

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        while left < right:

            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water_trapped += (left_max - height[left])
                left += 1
            else:
                right_max = max(right_max, height[right])
                water_trapped += (right_max - height[right])
                right -= 1

        return water_trapped

s = Solution()
res = s.trap([0,2,0,3,1,0,1,3,2,1])
print(res)

# 3.39 -> 7 min