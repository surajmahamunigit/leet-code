# 6.06

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """Evaluate the RPN and return the result.

        Args:
            tokens: list of str representing RPN

        Returns:
            answer to RPN

        Time: O(n) - n = len(tokens)
        Space: O(n)
        """
        stack = []

        for token in tokens:

            if token == "+":
                stack.append(stack.pop() + stack.pop())

            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif token == "*":
                stack.append(stack.pop() * stack.pop())

            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))

            else:
                stack.append(int(token))

        return stack[-1]

s = Solution()
assert s.evalRPN(["2","1","+","3","*"]) == 9
assert s.evalRPN(["4","13","5","/","+"]) == 6
assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
assert s.evalRPN(["-3","2","/"]) == -1        # int(-3/2) = -1, not -3//2 = -2
assert s.evalRPN(["5"]) == 5                   # single token
print("passed")


# 6.14 -> 8 minutes to finish