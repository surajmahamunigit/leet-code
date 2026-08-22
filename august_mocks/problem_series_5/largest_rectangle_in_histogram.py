#11.49
# given array of bar height and asked to find largest rectangle area created by bars
# use stack to store bar heights and index
# if curr bar height is longer than last one -> add to stack with index, height
# if bar curr height is smaller than last on -> pop last bar from stack -> calculate area for it -> compare -> add curr bar to stack
# with popped bar index, height
# when loop is over -> stack would still have bars
# start measuring area for each bar in stack and compare
# return max_are

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Find the largest rectangle area that fits within histogram.

        Args:
            heights: where heights[index] is bar height at index

        Returns:
            maximum rectangle area possible inside histogram

        Time: O(n) - n = len(heights)
        Space: O(n)
        """
        max_area = 0
        stack = []
        for index in range(len(heights)):
            curr_height = heights[index]
            start = index
            while stack and stack[-1][1] > curr_height:
                stack_index, stack_height = stack.pop()
                stack_area = (index - stack_index) * stack_height
                max_area = max(max_area, stack_area)
                start = stack_index

            stack.append([start, curr_height])

        # for remaining bars in stack
        for stack_index, stack_height in stack:
            stack_area = (len(heights) - stack_index) * stack_height
            max_area = max(max_area, stack_area)

        return max_area

s = Solution()
assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
assert s.largestRectangleArea([2,4]) == 4
assert s.largestRectangleArea([2,1,2]) == 3
assert s.largestRectangleArea([]) == 0
assert s.largestRectangleArea([5]) == 5
assert s.largestRectangleArea([1,2,3,4,5]) == 9
assert s.largestRectangleArea([5,4,3,2,1]) == 9
print("passed")

# 12.08 -> 19 min to solve