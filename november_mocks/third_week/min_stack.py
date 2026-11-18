# 8.44

class Solution:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # to track minimum values

    def push(self, val:int):
        """Pushes values to the stack.
            Time complexity: O(1)
            Space complexity: O(1)
        """
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self):
        """Pops last value from the stack.
            Time complexity: O(1)
            Space complexity: O(1)
        """

        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """Returns the last value in the stack.
            Time complexity: O(1)
            Space complexity: O(1)
        """

        return self.stack[-1]

    def get_min(self) -> int:
        """Returns the minimum value in the stack.
            Time complexity: O(1)
            Space complexity: O(1)
        """

        return self.min_stack[-1]

s = Solution()

s.push(2)
s.push(3)
s.push(1)
print(s.top())
print(s.get_min())

s.pop()
print(s.top())
print(s.get_min())