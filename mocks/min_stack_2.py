class MinStack:

    def __init__(self):
        self.stack = []     # to store each number
        self.min_stack = [] # to store min till that number

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()        # remove this number because we removed its number from stack

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.get_min()) # return 0
minStack.pop()
print(minStack.top())    # return 2
print(minStack.get_min()) # return 1
