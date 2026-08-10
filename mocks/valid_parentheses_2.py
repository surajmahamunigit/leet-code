# algorithm
# we will use stack to solve this problem. and close_map = {"}":"{", "]":"[", ")":"("}
# for every char in string, we will check if that char exist in close_map -> if yes, then we compare char's value with stack[-1]
# if its equal, then we pop the the last value from stack. if its not equal, we return False
# if value is not in close_map means its opening bracket, add it to the stack

class Solution:
    def valid_parentheses(self, s: str) -> bool:
        """Find if given string contains valid brackets.

        Args:
            s: input string containing brackets.

        Returns:
            True if brackets are in valid sequence, else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        close_map = {"}":"{", "]":"[", ")":"("}
        stack = []
        for char in s:
            if char in close_map:
                if close_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)
        return not stack

s = Solution()
#res = s.valid_parentheses(s = "[]")
#res = s.valid_parentheses(s = "([{}])")
res = s.valid_parentheses(s = "[(])")
print(res)