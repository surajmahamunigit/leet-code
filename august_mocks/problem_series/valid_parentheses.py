# 2.04
# given list of brackets and asked to find if they are in right order
# check if given bracket is in close_map = {"}":"{", "]":"[", ")":"("}
# if found pop stack[-1] and compare its values -> not same return False

class Solution:
    def isValid(self, s: str) -> bool:
        """Find out if list of given brackets are in right order.

        Args:
            s: string containing brackets

        Returns:
            True if brackets are in right order, else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """
        stack = []
        close_map = {"}": "{", "]": "[", ")": "("}

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
print("passed")

# 2.18 -> min to solve
# add this question on daily list for next 3 days