# 9.27

class Solution:
    def trapWater(self, height: list[int]) -> int:
        """Find the total water trapped between bars.

        Args:
            height (list[int]): integer array representing each bars height

        Returns:
            int: total water trapped between bars

        Time: O(n) - n = len(height)
        Space: O(1)
        """

        if len(height) <= 1:
            return 0
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
assert s.trapWater([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert s.trapWater([4,2,0,3,2,5]) == 9
assert s.trapWater([]) == 0
assert s.trapWater([5]) == 0
assert s.trapWater([1,1]) == 0
print('passed')