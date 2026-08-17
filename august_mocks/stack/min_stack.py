# 1.08

class MinStack:

    def __init__(self):
        self.stack = []         # to add each number
        self.min_stack = []     # to add minimum till current number

    def push(self, val: int) -> None:
        """Adds given value in the stack and minimum of stack till val.

        Args:
            val: integer value to add to stack

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
        """Removes top of list and also removes minimum till that number.

        Time: O(1)
        Space: O(1)
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """Returns the top number in the list.

        Time: O(1)
        Space: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """Returns minimum value in the list.

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
assert ms2.getMin() == 1   # duplicate-minimum trap
ms2.pop()
assert ms2.getMin() == 1
print("passed")

# 1.19 -> 11 min to finish