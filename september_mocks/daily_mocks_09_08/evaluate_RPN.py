# 7.52

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """Evaluate the given Reverse Polish Notion equation and return result.

        Args:
            tokens (list[str]): list representing RPN

        Returns:
            int: evaluates RPN and returns result

        Time: O(n) - n = len(tokens)
        Space: O(n))
        """

        stack = []

        for char in tokens:

            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))      # truncates towards zero
            else:
                stack.append(int(char))

        return stack[-1]

s = Solution()
assert s.evalRPN(["2","1","+","3","*"]) == 9
assert s.evalRPN(["4","13","5","/","+"]) == 6
assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
assert s.evalRPN(["-3","2","/"]) == -1
assert s.evalRPN(["5"]) == 5
print('passed')

# 7.59 -> 7 min