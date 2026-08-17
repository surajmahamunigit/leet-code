# 7.06

class Solution:
    def trapWater(self, height: list[int]) -> int:
        """Find out maximum water trapped between bars.

        Args:
            height: list of integer representing each bar height

        Returns:
            max water trapped between bars

        Time: O(n) - n = len(height)
        Space: O(1)
        """
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        max_water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                curr_max = (left_max - height[left])
                max_water += curr_max
                left += 1
            else:
                right_max = max(right_max, height[right])
                curr_max = (right_max - height[right])
                max_water += curr_max
                right -= 1

        return max_water

s = Solution()
assert s.trapWater([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert s.trapWater([4,2,0,3,2,5]) == 9
assert s.trapWater([]) == 0
assert s.trapWater([5]) == 0
assert s.trapWater([1,1]) == 0
print("passed")

# 7.21 -> 15 min to solve