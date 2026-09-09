# 4.11


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Find out if the given string is palindrome or not.

        Args:
            s: given string

        Returns:
            bool: True if string is palindrome else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        result = ""

        for char in s:

            if char.isalnum():
                result += char.lower()

        return result == result[::-1]


    def isPalindromeNoAlnum(self, s: str) -> bool:
        """Find out if the given string is palindrome or not.

        Args:
            s: given string

        Returns:
            bool: True if string is palindrome else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        result = ""

        for char in s:

            if self.isalphanumeric(char):
                result += char.lower()

        return result == result[::-1]

    def isalphanumeric(self, char: str) -> bool:
        """Find out if the given string is alphanumeric or not."""

        return ord("A") <= ord(char) <= ord("Z") or ord("a") <= ord(char) <= ord("z") or ord("0") <= ord(char) <= ord("9")



s = Solution()
assert s.isPalindromeNoAlnum("A man, a plan, a canal: Panama") == True
assert s.isPalindromeNoAlnum("race a car") == False
assert s.isPalindromeNoAlnum("") == True
assert s.isPalindromeNoAlnum("0P") == False
print("passed")