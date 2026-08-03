
# Algorithm
# create map with key-value pair -> close_ma = {")":"(", "]":"[", "}":"{"} and empty stack
# check each character in string s
# -> if char exists in close_map
# -> check if stack is not empty and stack[-1] == close_mpa[char] -> if True, pop stack[-1]. else return False  ->
# if character not present in map, means its opening bracket -> add it to the stack
# after for loop is over, return true if stack is empty else False

# example
# s = "()[]{}",
# s[0] -> ( -> stack = ["(",]
# s[1] -> ) -> exist in map -> pop stack -> True
# s[2] -> [ -> stack = ["["]
# s[3] -> ] -> exist in map -> pop stack -> True
# s[4] -> { -> stack = ["{"]
# # s[5] -> } -> exist in map -> pop stack -> True

class Solution:
    def isValid(self, s: str) -> bool:
        """Find out if given string conatins correct order and correctly nested brackets or not.

        Args:
            s: input string containing brackets

        Return:
            True if and only if given string contains correct order and correctly nested else False

        Time: O(n) - n = len(s)
        Space: O(n) - given s might have all opening brackets.
        """

        close_map = {")" : "(", "]" : "[", "}" : "{"}
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
assert s.isValid("()[]{}") == True
assert s.isValid("(]") == False
assert s.isValid("(") == False
assert s.isValid(")") == False
assert s.isValid("(((") == False
print("passed")