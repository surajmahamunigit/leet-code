class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """
        Args:
            heights: Integer array representing different heights

        Returns:
            int: Max area

        Time: O(n) - two-pointer strategy
        Space: O(1) - no extra space
        """

        result = 0
        left = 0
        right = len(heights) - 1

        while left < right:

            # Calculate current area
            current_area = (right - left) * min(heights[left], heights[right])

            # Compare with max area
            result = max(result, current_area)

            # Modify left or right, whichever has min height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result


result = Solution().maxArea([1,7,2,5,4,7,3,6])
print(result)