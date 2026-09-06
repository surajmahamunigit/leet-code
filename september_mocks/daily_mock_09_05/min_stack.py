# 8.27

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """Push given integer to the stack.

        Args:
            val (int): integer number to pushed to stack

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
        """pop last integer value from the stack.

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
        """Return the last integer value from the stack.

        Args:
            None

        Returns:
            int: last integer number from stack

        Time: O(1)
        Space: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """Return the smallest number in the stack.

        Args:
            None

        Returns:
            smallest number from the stack

        Time: O(1)
        Space: O(1)
        """
        return self.min_stack[-1]