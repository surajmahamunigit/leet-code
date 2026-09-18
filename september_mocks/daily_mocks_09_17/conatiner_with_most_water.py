# 6.29

class Solution:
    def max_area(self, heights: list[int]) -> int:
        """Fins the maximum container area.

        Args:
            heights (list[int]): integer array representing height of each bar

        Returns:
            int: maximum area of the container formed

        Time: O(n) - len(heights)

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
print(s.max_area(heights = [1,7,2,5,4,7,3,6]))
print(s.max_area(heights = [2,2,2]))
