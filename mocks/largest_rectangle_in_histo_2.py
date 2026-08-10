# Algorithm
# we are given array with heights
# here index of height and height matters and we will use it together.
# for each height at index i, -> start = i,
# while stack is not empty and curr_height is smaller than stack height -> pop the stack[-1] -> stack_area = (index - stack_index) * stack_height
# comapre with max_area and move the start for current index till stack index
# if stack is empty, add (index,height) to stack for later use.
# after for loop is over, stack might night be empty -> start poping stack[-1]
# for every entry in stack, calculate curr_area = (len(heights) - stack_index) * stack_height

class Solution:
    def largest_rectangle(self, heights: list[int]) -> int:
        """Find maximum area possible in given histogram.

        Args:
            heights: integer array representing height of each bar

        Returns:
            maximum area formed by rectangle in given histogram

        Time: O(n) - n = len(heights)
        Space: O(n) - for stack
        """
        max_area = 0
        stack = []   # to store (index, height) for each bar
        for index, height in enumerate(heights):
            start = index           # starting position of bar

            # if stack has bar in it
            # check new bar we are adding is bigger than last bar
            # otherwise remove the long bars before adding small bar
            while stack and stack[-1][1] > height:
                stack_index, stack_height = stack.pop()
                stack_bar_area = (index - stack_index) * stack_height       # for bar we are removing
                max_area = max(max_area, stack_bar_area)
                start = stack_index
            # if stack is empty add (index, height) t the stack
            stack.append((start, height))

        # now calculate area for bars that are still remaining in the stack
        for stack_index, stack_height in stack:
            stack_bar_area = (len(heights) - stack_index) * stack_height
            max_area = max(max_area, stack_bar_area)

        return max_area

s = Solution()
#res = s.largest_rectangle(heights = [7,1,7,2,2,4])
res = s.largest_rectangle(heights = [1,3,7])
print(res)