# 2.41

class Solution:
    def isValid(self, s: str) -> bool:
        """Find out if the given string has valid order of brackets.

        Args:
            s: input string containing brackets

        Returns:
              True if string has valid order of brackets, else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        stack = []
        close_map = {"}":"{", ")":"(", "]":"["}
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
assert s.isValid("()[]{}") == True
assert s.isValid("(]") == False
assert s.isValid("(") == False
assert s.isValid(")") == False
assert s.isValid("(((") == False
assert s.isValid("") == True
assert s.isValid("([)]") == False
assert s.isValid("(())") == True
assert s.isValid("([{}])") == True
print("passed")