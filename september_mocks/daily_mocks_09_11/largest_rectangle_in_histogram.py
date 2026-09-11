# 10.28
from ast import List


class Solution:
    def largestRectangleArea(self, height: list[int]) -> int:
        """Find the largest rectangle area in given histogram.

        Args:
            height (list[int]): list of integers representing height of each bar

        Returns:
            int: largest rectangle area formed in histogram.

        Time: O(n) - n = len(height)
        Space: O(n)
        """

        # [2,1,5,6,2,3]
        stack = []
        max_area = 0

        for index, value in enumerate(height):
            start = index
            while stack and stack[-1][1] >= value:
                stack_index, stack_value = stack.pop()
                curr_area = (index - stack_index) * stack_value
                max_area = max(curr_area, max_area)
                start = stack_index

            stack.append([start, value])

        # for remaining bars in stack
        for index, value in stack:
            curr_area = (len(height) - index) * value
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

# 10.42 -> 14 min
# make sure we repeat this problem at least every 4-5 days