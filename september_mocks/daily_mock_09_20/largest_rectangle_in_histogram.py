# 2.30

class Solution:
    def largest_rectangle_area(self, heights: list[int]) -> int:
        """Find the largest rectangle area in given histogram.

        Args:
            heights (list[int]): list representing height of each bar

        Returns:
            int: largest rectangle area in histogram

        Time:

        Space:
        """
        max_area = 0
        stack = []

        for index in range(len(heights)):
            start = index
            while stack and stack[-1][1] > heights[index]:
                stack_index, stack_height = stack.pop()
                curr_area = (index - stack_index) * stack_height
                max_area = max(curr_area, max_area)
                start = stack_index

            stack.append([start, heights[index]])

        # for remaining bars in stack
        for stack_index, stack_height in stack:
            curr_area = (len(heights) - stack_index) * stack_height
            max_area = max(curr_area, max_area)

        return max_area

s = Solution()
print(s.largest_rectangle_area(heights = [7,1,7,2,2,4]))
print(s.largest_rectangle_area(heights = [1,3,7]))

# 2.43 -> 13 min to solve