# 2.10
# given integer array representing height of each line, and aske dto find two lines that make biggest rectangle
# use two points pattern
# keep one pointer at left = 0 and second one at len(heights)
# calculate area -> record highest area value -> move pointer with smaller height


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """Find the largest area formed by two lines.

        Args:
            heights: heights[i] line height at index i

        Returns:
            largest area formed by two lines

        Time: O(n) - n = len(heights)
        Space: O(1)
        """

        largest = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            curr_area = (right - left) * min(heights[left], heights[right])

            largest = max(largest, curr_area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1


        return largest

s = Solution()
assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert s.maxArea([1,1]) == 1
assert s.maxArea([4,3,2,1,4]) == 16
assert s.maxArea([1,2,1]) == 2
print("passed")

# 2.19 -> 9 min to solve