# 8.17

class Solution:
    def is_valid(self, s: str) -> bool:
        """check if the given string s contains valid parentheses.

        Args:
            s: given string containing only parentheses

        Returns:
            bool: True if the string contains valid parentheses, else False

        Time complexity: O(n) - n = len(s)

        Space complexity: O(n)
        """

        # S = "{][}"

        closed_parentheses = {"]":"[", "}":"{", ")":"("}
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
    result = s.is_valid(values)
    assert result == expected

check("{", False)
check("}", False)
check("{]", False)
check("{}", True)
check("[{}]", True)
check("(()", False)
check("{[()]}", True)

print("all test passed")
