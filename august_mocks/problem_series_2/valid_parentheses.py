# 9.29
# given string of brackets, asked to check if their order is valid
# use stack patter -> if its opening bracket, add to stack, -> if its closing bracket, compare with stack[-1]

class Solution:
    def isValid(self, s: str) -> bool:
        """Determine if the given string has valid order of parentheses.

        Args:
            s: given string with brackets

        Returns:
            True if brackets order is valid, else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        stack = []
        close_map = {"}":"{", "]":"[", ")":"("}

        for char in s:
            if char in close_map :
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

# 9.40 -> 11 minute sto finish