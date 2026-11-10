# 11.32

class Solution:
    def __init__(self):
        """Initializes the stack class."""
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """Pushes a value onto the stack.

        Args:
            val: integer value to push
        Returns:
            None
        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        """Removes the last value from the stack.

        Args:

        Returns:
            None
        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """Returns the top value in the stack.

        Args:

        Returns:
            int: top value from the stack
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.stack[-1]

    def get_min(self) -> int:
        """Returns the minimum value in the stack.

        Args:

        Returns:
            int: minimum value from the stack
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.min_stack[-1]

s = Solution()

s.push(5)
s.push(3)
s.push(4)

s.push(1)
print(s.top())
print(s.get_min())
s.pop()
print(s.top())
print(s.get_min())