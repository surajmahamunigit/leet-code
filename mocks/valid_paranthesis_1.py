# algorithm
# create a dict with closing brackets as key and opening backets as value. close_map = {"}":"{", ']':'[', ')':'('}
# check every char at index is in close map -> if yes, close_map[char] == stack[-1], pop stck[-1], else return False
# otherwise add to the stack
# in end return True if stack is empty

class Solution:
    def isValid(self, s: str) -> bool:
        """Find given string s contains valid parathesis order or not.

        Args:
            s: input string containing brackets

        Returns:
            True if string s has valid brackets order, else False

        Time: O(n) - n = len(s)
        Space: O(n)

        """
        close_map = {"}":"{", ']':'[', ')':'('}
        stack = []

        for char in s:
            if char in close_map:
                if stack and close_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return not stack

s = Solution()
assert s.isValid("[]") == True
assert s.isValid("([{}])") == True
assert s.isValid("([{}]") == False
print("passed")