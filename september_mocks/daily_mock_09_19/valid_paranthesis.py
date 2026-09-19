# 3.07

class Solution:
    def is_valid(self, s: str) -> bool:
        """Find  if the given string contain valid order of parenthesis.

        Args:
            s (str): string containing parenthesis.

        Returns:
            bool: True if the given string contain valid order of parenthesis, else False.

        Time : O(n) - n = len(s)

        Space: O(n)
        """

        stack = []
        close_map = {")":"(", "]":"[", "}":"{"}
        for char in s:

            if stack and char in close_map:
                if stack[-1] == close_map[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return not stack

s = Solution()
print(s.is_valid(s = "[]"))
print(s.is_valid(s = "([{}])"))
print(s.is_valid(s = "[(])"))