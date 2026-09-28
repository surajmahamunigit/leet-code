# 3.27

class Solution:
    def largest_rectangle_area(self, heights: list[int]) -> int:
        """Find the largest rectangle area in give histogram.

        Args:
            heights (list[int]): list of integers representing each bars height in histogram

        Returns:
            int: largest rectangle area in histogram

        Time: O(n) - n = len(temperatures)

        Space: O(n)
        """

        # heights = [7,1,7,2,2,4]
        stack = []
        largest = 0
        for index in range(len(heights)):
            start = index
            while stack and stack[-1][1] > heights[index]:
                stack_index, stack_height = stack.pop()
                curr_area = (index - stack_index) * stack_height
                largest = max(largest, curr_area)

                start = stack_index

            stack.append([start, heights[index]])

        # for remaining bars in stack
        for stack_index, stack_height in stack:
            curr_area= (len(heights) - stack_index) * stack_height
            largest = max(largest, curr_area)

        return largest

s = Solution()
print(s.largest_rectangle_area(heights = [7,1,7,2,2,4]))
print(s.largest_rectangle_area(heights = [1, 1, 1]))
print(s.largest_rectangle_area(heights = []))