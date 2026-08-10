# algorithm
# given array representing RPN
# we wiil add numbers to stack and perform operation right away

class Solution:
    def RPN(self, tokens: list[str]) -> int:
        """Find answer to the RPN.

        Args:
            tokens: list of strings representing RPN

        Returns:
            answer to the RPN

        Time: O(n) - n = len(tokens)
        Space: O(n)
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
                stack.append(int(a / b))

            else:
                stack.append(int(char))

        return stack[-1]

s = Solution()
res = s.RPN(tokens = ["1","2","+","3","*","4","-"])
print(res)