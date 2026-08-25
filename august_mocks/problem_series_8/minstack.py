# 11.37

class MinStack:

    def __init__(self):
        self.stack = []     # keep track of all numbers
        self.min_stack = []     # keep track of minimum num

    def push(self, val: int) ->  None:
        """Pushes given integer value in stack.

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
        """Remove the last number from stack.

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
        """Returns last value in the stack.

        Args:
            None

        Returns:
            last integer value

        Time: O(1)
        Space: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """Returns smallest value in the stack.

        Args:
            None
        Returns:
            smallest integer value in stack

        Time: O(1)
        Space: O(1)
        """
        return self.min_stack[-1]

# 11.47 -> 10 min to solve