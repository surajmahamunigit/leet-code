# 5.49

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Find the largest rectangular area formed in histogram.

        Args:
            heights (list[int]): list of integers representing height of each bar

        Returns:
            int: largest rectangle area

        Time: O(n) - n = len(heights)
        Space: O(n)
        """

        # 2,1,5,6,2,3
        max_area = 0
        stack = []
        for index, height in enumerate(heights):
            start = index

            while stack and stack[-1][1] > height:

                stack_index, stack_height = stack.pop()

                curr_area = (index - stack_index) * stack_height
                max_area = max(curr_area, max_area)
                start = stack_index

            stack.append([start, height])

        # for remaining bars in stack
        for index, height in stack:
            curr_area = (len(heights) - index) * height
            max_area = max(curr_area, max_area)

        return max_area

s = Solution()
assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
assert s.largestRectangleArea([2,4]) == 4
assert s.largestRectangleArea([2,1,2]) == 3
assert s.largestRectangleArea([]) == 0
assert s.largestRectangleArea([5]) == 5
assert s.largestRectangleArea([1,2,3,4,5]) == 9
assert s.largestRectangleArea([5,4,3,2,1]) == 9
print('passed')