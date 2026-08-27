#4.26
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """To push the given val in stack.

        Args:
            val: integer value

        Returns:
            None

        Time: O(1)
        Space: O(1)
        """
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        """Pop last value from the stack.

        Args: None
        Returns: None

        Time: O(1)
        Space: O(1)
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """Returns last value in stack.

        Args:
            None

        Returns:
            last value in stack

        Time: O(1)
        Space: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """Returns smallest number in stack.
        Args:
            None

        Returns:
            smallest value in stack

        Time: O(1)
        Space: O(1)
        """
        return self.min_stack[-1]

# 4.32 -> 6 min to solve