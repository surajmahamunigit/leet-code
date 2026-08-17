# 4.40

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """Evaluate the given reverse polish notion equation and return result.

        Args:
            tokens: array representing RPN

        Returns:
            result of RPN

        Time: O(n) - n = len(tokens)
        Space: O(n)
        """
        stack = []

        for index in range(len(tokens)):
            if tokens[index] == "+":
                stack.append(stack.pop() + stack.pop())

            elif tokens[index] == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif tokens[index] == "*":
                stack.append(stack.pop() * stack.pop())

            elif tokens[index] == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))          # truncates towards zero

            else:
                stack.append(int(tokens[index]))

        return stack[-1]

s = Solution()
assert s.evalRPN(["2","1","+","3","*"]) == 9
assert s.evalRPN(["4","13","5","/","+"]) == 6
assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
assert s.evalRPN(["-3","2","/"]) == -1
assert s.evalRPN(["5"]) == 5
print("passed")

# 4.57 -> 17 min to solve
