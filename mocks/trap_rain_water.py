# Algorithm:
# given height = [0,1,0,2,1,0,1,3,2,1,2,1]
# two pointers left = 0, right = len(height), assume left_max = height[0], right_max = height[11]
# while left < right ->
# compare height[left] and height[right] ->
# if height[left] <= height[right] -> move left forward, calculate new left_max=max(left_max,height[left]), calculate water trapped = left_max - height[left]
# else move right inward, calculate new right_max, calculate water trapped
# when outside while loop fails, we would have covered all bars and calculated water trapped. so return water trapped.





# height[left] <= height[right] -> 2<=1 -> right=10,right_max=2,water_trapped=2-2=0
class Solution:
    def trapWater(self, height: list[int]) -> int:
        """Compute the total water trapped between the bars.

        Args:
            height: list containing bar heights

        Returns:
            total water trapped between bars after rain.

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
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]

            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]

        return water_trapped

s = Solution()
assert s.trapWater([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
print("passed")


