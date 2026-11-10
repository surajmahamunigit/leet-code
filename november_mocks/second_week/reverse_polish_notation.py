# 12.52

class Solution:
    def eval_rpn(self, tokens: list[str]) -> int:
        """Evaluate the given Reverse Polish Notation.

        Args:
             tokens: list of string representing valid Reverse Polish Notation

        Returns:
            str: result of the given reverse polish notation

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
                stack.append(int(a / b))    # truncate towards zero
            else:
                stack.append(int(char))
        return stack[-1]

s = Solution()

def check(values, expected):
    result = s.eval_rpn(values)
    assert result == expected

check(["1", '2', "+"], 3)
check(['3', "1", '-'], 2)
check(['3', '3', '*'], 9)
check(['12', '3', "/"], 4)
check(["-20", '6', "/"], -3)
check(['0', '0', '+'], 0)