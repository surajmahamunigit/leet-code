# 6.49

class Solution:
    def trapWater(self, height: list[int]) -> int:
        """Find out water trapped between bars.

        Args:
            height (list[int]): a list of integers representing individual bar height

        Returns:
            int: total water trapped between bars

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
                water_trapped += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
                right -= 1

        return water_trapped

s = Solution()
print(s.trapWater(height = [0,2,0,3,1,0,1,3,2,1]))
#print(s.trapWater())