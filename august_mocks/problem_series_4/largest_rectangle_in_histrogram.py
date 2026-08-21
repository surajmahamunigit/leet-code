# 12.12
# given bar heights and asked to find out largest rectangle area created by histogram.

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Find the area of largest rectangle that fits inside histogram.

        Args:
            heights: list of integers representing bar height

        Returns:
            largest rectangle that fits inside histogram.

        Time: O(n) - n = len(heights)
        Space: O(n)
        """

        stack = []
        largest = 0
        for index, height in enumerate(heights):
            start = index
            while stack and heights[index] < stack[-1][1]:
                stack_index, stack_height = stack.pop()
                curr_area = (index - stack_index) * stack_height
                largest = max(curr_area, largest)
                start = stack_index

            stack.append((start, height))

        # remove the bars from stack
        for stack_index, stack_height in stack:
            curr_area = (len(heights) - stack_index) * stack_height
            largest = max(curr_area, largest)

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

# 12.30 -> 18 min to solve
# add this problem for two more repetitions for next two days