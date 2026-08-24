# 1.27
# we are asked to write functions push, pop, top and getMin with O(1) time complexity

class MinStack:
    def __init__(self):
        self.stack = []         # to store each number
        self.min_stack = []     # to store minimum

    def push(self, val: int) -> None:
        """To push number into stack.

        Args:
            val: given number

        Returns:
            None

        Time: O(1)
        Space: O(1)
        """
        self.stack.append(val)

        if self.min_stack:
            self.min_stack(min(self.min_stack[-1]), val)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        """Pop last number in stack.

        Args:
            None
        Returns:
            None

        Time: O(1)
        Space: O(1)
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """Return last number in stack.

        Args:
            None

        Returns:
            last number in stack

        Time: O(1)
        Space: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """Return the smallest number in the stack.

        Args:
            None

        Return:
            smallest number in stack

        Time: O(1)
        Space: O(1)
        """
        return self.min_stack[-1]

# 1.36 -> 9 min to solve