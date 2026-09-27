# 2.52

class Solution:
    def trap_water(self, height: list[int]) -> int:
        """Find the total water trapped between the bars.

        Args:
            height(list[int]): list of integers representing the height of each bar

        Returns:
            int: total water trapped between the bars

        Time: O(n) - n = len(nums)

        Space: O(1)
        """

        # height = [0,2,0,3,1,0,1,3,2,1]

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
print(s.trap_water([5,4,3,2,1, 2]))
print(s.trap_water([1]))