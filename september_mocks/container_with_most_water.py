# 11.24

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """Find the maximum rectangular area formed by two lines.

        Args:
            heights: integer array representing height of each line

        Returns:
            maximum rectangular area formed by two lines

        Time: O(n) - n = len(heights)
        Space: O(1)
        """

        max_area = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            curr_area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, curr_area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

s = Solution()
assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert s.maxArea([1,1]) == 1
assert s.maxArea([4,3,2,1,4]) == 16
assert s.maxArea([1,2,1]) == 2
print('passed')


# 11.31 -> 7 min