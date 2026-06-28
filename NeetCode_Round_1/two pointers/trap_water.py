class Solution:
    def trapWater(self, height: list[int]) -> int:
        """
        Args:
            height: Integer array representing heights

        Returns:
            total water trapped

        Time: O(n) - two pointer pattern
        Space: O(1) - no extra space
        """

        result = 0
        left = 0
        left_max = height[left]
        right = len(height) - 1
        right_max = height[right]

        while left < right:

            # Compare both heights
            if height[left] < height[right]:
                left += 1
                # New left_max
                left_max = max(left_max, height[left])
                # Water trapped
                result = result + (left_max - height[left])

            else:
                right -= 1
                # New right_max
                right_max = max(right_max, height[right])
                # Water trapped
                result = result + (right_max - height[right])

        return result

result = Solution().trapWater([0,2,0,3,1,0,1,3,2,1])
print(result)