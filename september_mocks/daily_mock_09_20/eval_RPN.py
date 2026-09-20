# 2.54

class Solution:
    def eval_RPN(self, tokens: list[str]) -> int:
        """Evaluate the given RPN and return result.

        Args:
            tokens (list[str]): list representing RPN

        Returns:
            int: result of the given RPN

        Time: O()

        Space: O()
        """

        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b = stack.pop()
                a  = stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))      # truncate to zero
            else:
                stack.append(int(token))

        return stack[-1]

s = Solution()
print(s.eval_RPN(tokens = ["1","2","+","3","*","4","-"]))
