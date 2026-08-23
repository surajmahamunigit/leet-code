# 1
# given heights array that contains bars with height and width is 1 and asked to find out largest rectangle histrogram possible


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Find the largest rectangle area formed in given histogram.

        Args:
            heights: array of integers representing bar heights

        Returns:
            largest rectangle area formed in histogram

        Time: O(n) - len(heights)
        Space: O(n)
        """

        stack = []
        max_area = 0

        for index in range(len(heights)):
            start = index
            curr_height = heights[index]
            if stack and stack[-1][1] > curr_height:
                stack_index, stack_height = stack.pop()
                stack_area = (index - stack_index) * stack_height
                max_area = max(max_area, stack_area)
                start = stack_index

            stack.append((start, curr_height))

        # for unpopped bars
        for stack_index, stack_height in stack:
            stack_area = (len(heights) - stack_index) * stack_height
            max_area = max(max_area, stack_area)

        return max_area

# 1.11 -> 11 min to solve