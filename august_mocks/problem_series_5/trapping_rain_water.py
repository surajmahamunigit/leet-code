# 2.20
# two pointer pattern
# two pointers at left = 0, left_max = height[left], right = len(height), right_max = height[right]
# if left height <= right height ->for current left bar find out current left_max -> calculate water stored at current bar = left_max - curr_height , add to result and move left forward
# if not , calculate water stored at on right side bar
# return result

class Solution:
    def trapWater(self, height: list[int]) -> int:
        """Find the total water trapped between bars.

        Args:
            height: array representing each bars height

        Returns:
            total water trapped between bars

        Time: O(n) - n = len(height)
        Space: O(1)
        """

        result = 0

        if not height:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if height[left] <= height[right]:
                water_trapped = (left_max - height[left])
                result += water_trapped
                left += 1
            else:
                water_trapped = (right_max - height[right])
                result += water_trapped
                right -= 1

        return result
s = Solution()
assert s.trapWater([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert s.trapWater([4,2,0,3,2,5]) == 9
assert s.trapWater([]) == 0
assert s.trapWater([5]) == 0
assert s.trapWater([1,1]) == 0
print("passed")
# 2.35 -> 15 min to solve