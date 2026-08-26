# 1.24

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Find the largest rectangular area that can be formed inside given histogram.

         Args:
             heights: where heights[i] represents height of bar at index i

         Returns:
             maximum rectangle area

         Time:
         Space:
         """
        max_area = 0
        stack = []


        for index in range(len(heights)):
            start = index

            while stack and heights[index] <= stack[-1][1]:
                stack_index, stack_height = stack.pop()
                curr_area = (index - stack_index) * stack_height
                max_area = max(max_area, curr_area)
                start = stack_index

            stack.append([start, heights[index]])

        # for remaining bars in stack
        for stack_index, stack_height in stack:
            curr_area = (len(heights) - stack_index) * stack_height
            max_area = max(max_area, curr_area)

        return max_area

s = Solution()
res = s.largestRectangleArea([7,1,7,2,2,4])
print(res)
# 1.40