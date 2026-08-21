# 11.13
# given string s that contains opening and closing brackets, our job is to find out if the order of brackets is valid.
# if its close bracket -> check close_map[char] == stack[-1] -> True -> Pop stack -> else -> False
# else opening bracket add to stack

class Solution:
    def isValid(self, s: str) -> bool:
        """Find out the order of brackets given in string s is valid or not.

        Args:
            s: given string with brackets

        Returns:
            check brackets order and return True if valid order, else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        close_map = {"}":"{", "]":"[", ")":"("}
        stack = []

        for char in s:
            # char is closing bracket
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

# 11.23 -> 10 min to solve