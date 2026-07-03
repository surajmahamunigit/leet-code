class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Args:
            tokens: list of string representing RPN equation

        Returns:
            integer value after evaluating RPN equation

        Time: O(n) - n = len(tokens)
        Space: O(n)

        """
        stack = []

        for char in tokens:

            if char == "+":
                # Pop last two nums and add
                stack.append(stack.pop() + stack.pop())

            elif char == "-":
                b = stack.pop() # 2nd num
                a = stack.pop() # 1st num
                stack.append(a - b)

            elif char == "*":
                stack.append(stack.pop() * stack.pop())

            elif char == "/":
                b = stack.pop() # 2nd num
                a = stack.pop() # 1st num
                stack.append(int(a / b))    # truncate towards zero

            else:
                stack.append(int(char))     # str array given

        return stack[0]

result = Solution().evalRPN(["2", "1", "+", "3", "*", "4", "-"])
print(result)