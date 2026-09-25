# 12.09

class Solution:
    def valid_palindrome(self, s: str) -> bool:
        """Find out if the given string is palindrome or not.

        Args:
            s (str): given string

        Returns:
            bool: True if the given string is palindrome else False.

        Time: O(n) - n = len(s)

        Space: O(n)
        """

        result = ""

        for char in s:
            if char.isalnum():
                result += char.lower()

        return result == result[::-1]

    def valid_palindrome_no_space(self, s: str) -> bool:

        if len(s) <= 1:
            return True

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True