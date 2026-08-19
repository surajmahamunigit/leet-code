# 12.19
# asked to write MinStack class with push, pop, top, getMin function with O(1) time complexity


class MinStack:
    def __init__(self):
        self.stack = []             # add new number to list
        self.min_stack = []         # for minimum number

    def push(self, val: int) -> None:
        """Adds new value to stack.

        Args:
            val: integer number

        Returns:
            None

        Time: O(1)
        Space: O(1)
        """
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        """Removes the last value from stack.

        Args: None
        Returns: None

        Time: O(1)
        Space: O(1)
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """Returns last value in the stack.

        Args: None

        Returns:
            last value in the stack

        Time: O(1)
        Space: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """Returns smallest value in the stack.

        Args: None

        Returns:
            smallest value in the stack

        Time: O(1)
        Space: O(1)
        """
        return self.min_stack[-1]

ms = MinStack()
ms.push(-2); ms.push(0); ms.push(-3)
assert ms.getMin() == -3
ms.pop()
assert ms.top() == 0
assert ms.getMin() == -2

ms2 = MinStack()
ms2.push(1); ms2.push(2); ms2.push(1)
assert ms2.getMin() == 1
ms2.pop()
assert ms2.getMin() == 1
ms2.pop()
assert ms2.getMin() == 1

print("passed")

# 12.30 -> 11 min to solve