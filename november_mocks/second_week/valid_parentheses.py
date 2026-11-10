# 11.10

class Solution:
    def valid_parentheses(self, s: str) -> bool:
        """Find if the given string has valid parentheses.

        Args:
            s: given string containing parentheses

        Returns:
            bool: True if string s has valid parentheses, else False

        Time complexity: O(n) - n = len(s)

        Space complexity: O(n)
        """

        closed_parentheses = {"}":"{", "]":"[", ")":"("}
        stack = []

        for char in s:

            if char in closed_parentheses:
                if stack and closed_parentheses[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack

s = Solution()

def check(values, expected):
    result = s.valid_parentheses(values)
    assert result == expected

check("]", False)
check("[", False)
check("[}", False)
check("[]", True)
check("[])", False)
check("(()", False)
check("((({)))", False)
print("all tests passed")