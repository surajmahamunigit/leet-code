# 1.34

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Find the largest area that fits withing histogram.

         Args:
             heights: heights[i] bar height at ith index

         Returns:
             largets rectangle area

         Time: O(n) - n = len(heights)
         Space: O(n)
         """
        max_area = 0
        stack = []

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                stack_index, stack_height = stack.pop()
                curr_area = (index - stack_index) * stack_height
                max_area = max(max_area, curr_area)
                start = stack_index

            stack.append([start, height])

        while stack:
            stack_index, stack_height = stack.pop()
            curr_area = (len(heights) - stack_index) * stack_height
            max_area = max(max_area, curr_area)

        return max_area

s = Solution()
assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
assert s.largestRectangleArea([2,4]) == 4
assert s.largestRectangleArea([2,1,2]) == 3        # the extended-start-index trap
assert s.largestRectangleArea([]) == 0
assert s.largestRectangleArea([5]) == 5
assert s.largestRectangleArea([1,2,3,4,5]) == 9    # strictly increasing
assert s.largestRectangleArea([5,4,3,2,1]) == 9    # strictly decreasing
print("passed")

# 1.54 -> 20 min to solve