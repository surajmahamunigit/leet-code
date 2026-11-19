# 3.24

class Solution:
    def largest_rectangle(self, heights: list[int]) -> int:
        """Return largest rectangle area in the given histogram.

        Args:
            heights: list representing each bar height
        Returns:
            int: largest rectangle are possible in the given histogram
        Time complexity: O(n) - n = len(heights)
        Space complexity: O(n)
        """

        # heights = [1,2,4,0,2,1]

        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            start = index
            while stack and height <= stack[-1][1]:
                    prev_index, prev_height = stack.pop()
                    max_area = max(max_area, (index - prev_index) * prev_height)
                    start = prev_index
            stack.append((start, height))

        for prev_index, prev_height in range(len(stack) - 1, -1, -1):
            max_area = max(max_area, (len(heights) - prev_index) * prev_height)

        return max_area

