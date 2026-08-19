# 9.36
# asked to write a class with push, pop, top, getmin functions with O(1) time complexity
# use to stacks

class Solution:
    def __init__(self):
        self.stack = []     # for numbers
        self.min_stack = [] # for minimum number

    def push(self, val: int) -> None:
        """To add value into stack.
        Time: O(1)
        Space: O(1)
        """
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        """to remove last value from the stack.
        Time: O(1)
        Space: O(1)
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """Returns the last value in the stack.
        Time: O(1)
        Space: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """Returns minimum value in the stack.

        Time: O(1)
        Space: O(1)
        """
        return self.min_stack[-1]

# 9.43 -> 7 min to finish
