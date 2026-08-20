# 9.53
# given string that contains brackets, and we are asked to validate the order of brackets.
# for every char in s,
# check if char is in close_map ->
#   then check stack is not empty and stack[-1] == close_map value
#           if true -> pop char from stack
#           if not same -> return False
# else its opening bracket -> add to the stack
# in end check if stack is empty or not

class Solution:
    def isValid(self, s : str) -> bool:
        """Determine the given string has valid order of brackets or not.

        Args:
            s: given string containing brackets as char

        Returns:
            True if brackets are in valid order, else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        stack = []

        close_map = {"}":"{", "]":"[", ")":"("}
        for char in  s:

            # if char in closing bracket
            if char in close_map:
                if stack and stack[-1] == close_map[char]:
                    stack.pop()
                else:
                    return False

            # its opening bracket
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