# algorithm
# task is to design MinStack class with push, pop, top, getMin functions and O(1) time complexity
# first have two stack initialized in constructor, stack and min_stack
# void push(int val) -> pushes val to the stack
# if min_stack not empty, compare min(val, min_stack[-1]) and append it to min stack else append val to min_stack
# void pop() -> pops stack[-1] and min_stack[-1], returns nothing
# int top() -> returns stack[-1]
# int getMin() -> returns min_stack[-1]

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int):
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


m = MinStack()
m.push(1)
m.push(2)
m.push(0)
print(m.getMin())   # 0

m.pop()
print(m.top())      # 2
print(m.getMin())   # 1