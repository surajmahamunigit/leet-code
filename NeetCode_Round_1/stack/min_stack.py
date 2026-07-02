class MinStack:
    """
    Custom MinStack class with push, pop, top and getMin functions with runtime O(1)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Find new minimum and add it at top of min_stack
        min_value = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        """Return the minimum element in the stack."""
        return self.min_stack[-1]


s = MinStack()

s.push(1)
s.push(2)
s.push(3)
s.push(0)
print(f"top: {s.top()}")
print(f"minimum: {s.getMin()}")

s.pop()
print(f"top: {s.top()}")
print(f"minimum: {s.getMin()}")