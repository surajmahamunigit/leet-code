# 9.27

class Solution:
    def evaluate_reverse_polish_notation(self, tokens: list[str]) -> int:
        """Evaluate the given reverse polish notation and return the result.

        Args:
            tokens: given reverse polish notation

        Returns:
            int: result of reverse polish notation

        Time complexity: O(n) - n = len(tokens)

        Space complexity: O(n)
        """

        # tokens = ["2","3","+"]

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
                stack.append(int(a/b))  # truncates to zero
            else:
                stack.append(int(char))

        return stack[-1]

s = Solution()

def check(values, expected):
    result = s.evaluate_reverse_polish_notation(values)
    assert result == expected

check(["1","2","+"], 3)
check(["2", "3", "/"], 0)
check(["5", "2", "*", "10", "/", "5", "+"], 6)
check(["2", "3", "+", "6", "-", "2","+"], 1)
check(["1","2", "*", "1", "-", "1", "+"], 2)
print("all tests passed")