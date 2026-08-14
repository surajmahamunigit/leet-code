# 12.00

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """Find maximum area we can form to hold water using given array.

        Args:
            heights: list containing height of line

        Returns:
             maximum area

        Time: O(n) - n = len(heights)
        Space: O(1)
        """
        max_area = 0

        left = 0
        right = len(heights) - 1
        while left < right:
            curr_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, curr_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

s = Solution()
assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert s.maxArea([1,1]) == 1
assert s.maxArea([4,3,2,1,4]) == 16
assert s.maxArea([1,2,1]) == 2
print("passed")

# 12.07 -> 7 min to finish