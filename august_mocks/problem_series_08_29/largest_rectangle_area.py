# 10.44

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Find the largest rectangle area that fits within histogram.

        Args:
            heights: integer array representing bar height

        Returns:
            largest rectangle area that fits within histogram

        Time: O(n) - n = len(heights)
        Space: O(n)
        """

        largest = 0
        stack = []
        for index in range(len(heights)):
            start = index
            while stack and stack[-1][1] >= heights[index]:
                stack_index, stack_height = stack.pop()
                curr_area = (index - stack_index) * stack_height
                largest = max(largest, curr_area)
                start = stack_index

            stack.append([start, heights[index]])

        # remaining bars
        for stack_index, stack_height in stack:
            curr_area = (len(heights) - stack_index) * stack_height
            largest = max(largest, curr_area)

        return largest

s = Solution()
assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
assert s.largestRectangleArea([2,4]) == 4
assert s.largestRectangleArea([2,1,2]) == 3
assert s.largestRectangleArea([]) == 0
assert s.largestRectangleArea([5]) == 5
assert s.largestRectangleArea([1,2,3,4,5]) == 9
assert s.largestRectangleArea([5,4,3,2,1]) == 9
print("passed")

# 10.58 -> 14 min to solve