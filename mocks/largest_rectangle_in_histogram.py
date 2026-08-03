# Algorithm
# given heights = [2,1,5,6,2,3]
# max_area = 0, stack = [] and start from index 0 till len(heights)
# start = index -> for width
# while stack is not empty, and stack height is greater than current height means we cant extend previous bar further while calculating max_area
# pop bar from stack -> calculate area and compare with max_area -> then make start pointer point to stack_index meaning this bar could extend backward
# if stack is empty or current height > previous bar height , then just add the bar to the stack as (bar_index, bar_height)
# after for loop is over stack will have bars with increasing heights -> start popping one bar at time and calculate max_area for it and compare with max_area
# in end return max_Area

# example
# heights = [2,1,5,6,2,3], stack = [], max_area = 0
# index = 0 -> start = 0 -> stack is empty -> stack = [(0,2)] -> (start, heights[index])
# index = 1, -> start = 1 -> 1 < 2, pop stack -> current_area = stack_height * (index - stack_index) = 2 * (1-0)= 2, max_area = 2, start = stack_index = 0 -> stack = [(0,1)]
# index = 2 -> start= 2 -> 5>1 -> stack = [(0,1), (2,5)]
# index = 3 -> 6> 5 -> stack = [(0,1), (2,5), (3, 6)]
# index = 4 -> 2 < 6 -> pop stack -> current_area = 6 * (4-3) = 6, max_area = 6, start = 3
# index = 4 -> 2 < 5 -> pop stack -> curr_area = 5 * (4-2) = 10, max_area = 10, start = 2 -> stack = [(0, 1), (2, 2)]
# index = 5 -> 3 > 2 -> add to stack -> [(0, 1), (2, 2), (5, 3)]
# pop last bar (5,3)-> curr_area = 3 * (6-5) = 3
# pop (2,2) -> curr_area = 2 * (6-2) = 8, max_area = 8
# pop (0,1) -> curr_area = 1 * (6 -0) = 6
# max_area = 10


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Find the largest rectangle area in given histogram.

        Args:
            heights: list of int representing bar heights

        Returns:
            largest rectangle area

        Time: O(n) - n = len(heights)
        Space: O(n)
        """

        max_area = 0
        stack = []

        for index, height in enumerate(heights):

            start = index

            while stack and height < stack[-1][1]:
                stack_index, stack_height = stack.pop()
                stack_area = stack_height * (index - stack_index)
                max_area = max(max_area, stack_area)
                start = stack_index

            stack.append((start,height))

        for stack_index, stack_height in stack:
            stack_area = stack_height * (len(heights) - stack_index)
            max_area = max(max_area, stack_area)

        return max_area

s = Solution()
assert s.largestRectangleArea(heights = [2,1,5,6,2,3]) == 10
assert s.largestRectangleArea(heights = [2,4]) == 4
print("passed")