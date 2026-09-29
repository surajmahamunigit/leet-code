# 4.08

class Solution:
    def is_valid(self, s: str) -> bool:
        """Find out if the given string s contains valid parentheses.

        Args:
            s (str): given string containing opening and closing parentheses

        Returns:
            bool: True if the string s contain valid order of parentheses else False

        Time complexity: O(n) - n = len(s)

        Space complexity: O(n)
        """

        close_map = {"}":"{", "]":"[", ")":"("}
        stack = []
        for char in s:
            if char in close_map:
                if stack and stack[-1] == close_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack

s = Solution()
print(s.is_valid("{(})"))
print(s.is_valid("(()"))
print(s.is_valid("()()"))
print(s.is_valid("))"))
