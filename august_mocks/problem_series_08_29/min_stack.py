# 8.27

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """Push the given value in to the stack.

        Args:
            val = given integer value
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
        """Pop the last value in the stack.

        Args: None
        Returns: None
        Time: O(1)
        Space: O(1)
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """Returns the value of last number in stack.
        Args: None
        Returns: last integer value
        Time: O(1)
        Space: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """Returns the smallest value in the stack.
        Args: None
        Returns: smallest value in the stack
        Time: O(1)
        Space: O(1)
        """
        return self.min_stack[-1]

# 8.32 - > 5 min