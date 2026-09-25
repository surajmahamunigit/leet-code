# 11.50

class Solution:
    def max_water(self, heights: list[int]) -> int:
        """Find maximum water container.

        Args:
            heights (list[int]): a list of integers representing height of each bar at ith place.

        Returns:
              int: container area with maximum water

        Time : O(n) - n = len(heights)

        Space: O(1)
        """

        # height = [1,7,2,5,4,7,3,6]

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
print(s.max_water(heights = [1,7,2,5,4,7,3,6]))
print(s.max_water(heights = [2,2,2]))
# 11.56 -> 6  min