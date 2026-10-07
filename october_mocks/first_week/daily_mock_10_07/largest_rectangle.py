# 9.57

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Find the largest rectangle area in the given histogram.

        Args:
            heights (list[int]): list of integers representing individual bar height

        Returns:
            int: largest rectangle area in the given histogram

        Time complexity: O(n) - n = len(heights)

        Space complexity: O(n)
        """

        stack = []
        max_area = 0
        for index, height in enumerate(heights):

            start = index
            while stack and stack[-1][1] > height:
                stack_index, stack_height = stack.pop()
                stack_area = (index - stack_index) * stack_height
                max_area = max(max_area, stack_area)
                start = stack_index

            stack.append([start, height])

        # for remaining bars in stack
        for stack_index, stack_height in stack:
            stack_area = (len(heights) - stack_index) * stack_height
            max_area = max(max_area, stack_area)

        return max_area

# 10.10 -> 13 minutes to solve
# git commit message -> feat: add largest rectangle in histogram solution

s = Solution()
assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
assert s.largestRectangleArea([2,4]) == 4
assert s.largestRectangleArea([2,1,2]) == 3
assert s.largestRectangleArea([]) == 0
assert s.largestRectangleArea([5]) == 5
assert s.largestRectangleArea([1,2,3,4,5]) == 9
assert s.largestRectangleArea([5,4,3,2,1]) == 9
assert s.largestRectangleArea([4,4,4,4]) == 16
assert s.largestRectangleArea([2,2,2,1,2,2,2]) == 7