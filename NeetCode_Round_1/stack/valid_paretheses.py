class Solution:
    def isValid(self, s: str) -> bool:
        """
        Args:
            s: input string

        Returns:
            True if string s is valid, otherwise False

        Time:
        Space:
        """
        stack = []
        close_map = {"}":"{", "]":"[", ")":"("}

        for char in s:

            # if char is present in close_map
            if char in close_map:
                if stack and stack[-1] == close_map[char]:
                    stack.pop()
                else:
                    return False
            # if char not present in close_map
            else:
                stack.append(char)

        return not stack

result = Solution().isValid("{[()]}")
print(result)