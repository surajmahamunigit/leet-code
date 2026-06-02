"""
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def trapWater(self, height: list[int]) -> int:

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        result = 0

        while left < right:

            # Shift left or right index based on left_max and right_max
            if left_max < right_max:

                left += 1
                left_max = max(left_max, height[left])      # check new max after increment
                result += left_max - height[left]       # find water trapped for new height

            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]

        return result

result = Solution().trapWater([0, 2, 0, 3, 1, 0, 1, 3, 2, 1])
print(f"Total water trapped is {result}")