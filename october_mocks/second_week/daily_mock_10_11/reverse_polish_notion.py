# 2.58

# given reverse polish notion
# returns result of equation

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """Evaluate reverse polish notion and return result.

        Args:
            tokens (list[str]): given reverse polish notion equation

        Returns:
            int: result of the reverse polish notion

        Time complexity: O(n) - n = len(tokens)

        Space complexity: O(n)
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
                stack.append(int(a / b))        # truncate to zero
            else:
                stack.append(int(char))
        return stack[-1]

# 3.04 -> 6 minute sto solve problem
# git commit -> feat: add evaluate reverse polish notation solution

s = Solution()
assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
assert s.evalRPN(["3", "-4", "+"]) == -1
assert s.evalRPN(["7", "-2", "/"]) == -3
assert s.evalRPN(["-7", "2", "/"]) == -3
assert s.evalRPN(["-7", "-2", "/"]) == 3
assert s.evalRPN(["7", "2", "/"]) == 3
assert s.evalRPN(["0", "3", "/"]) == 0
assert s.evalRPN(["5"]) == 5
assert s.evalRPN(["-5"]) == -5
assert s.evalRPN(["3", "4", "-"]) == -1
assert s.evalRPN(["4", "3", "-"]) == 1
assert s.evalRPN(["2", "3", "4", "*", "+"]) == 14
assert s.evalRPN(["15", "7", "1", "1", "+", "-", "/", "3", "*", "2", "1", "1", "+", "+", "-"]) == 5
assert s.evalRPN(["1"] + ["1", "+"] * 10000) == 10001