class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Args:
            heights: list representing bar heights

        Returns:
            max area for rectangle

        Time: O(n) - n = len(heights)
        Space: O(n) - for stack
        """

        max_area = 0
        stack = []      # to store (index, height) as pair for each bar

        for current_index, current_height in enumerate(heights):

            # mark the start for current bar
            start = current_index

            # if previous bar height > current bar height
            while stack and current_height < stack[-1][1]:

                stack_index, stack_height = stack.pop()

                # Calculate max area for bar we are popping
                max_area = max(max_area, (stack_height * (current_index - stack_index)))

                # change the start for current bar
                start = stack_index

            # add the current_bar to stack
            stack.append((start, current_height))


        # Check max_area for bars in stack
        for i, h in stack:
            max_area = max(max_area, (h * (len(heights) - i)))


        return max_area

result = Solution().largestRectangleArea([7,1,7,2,2,4])
print(result)
