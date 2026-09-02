# 11.32

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """Determine if the given string is palindrome or not.

        Args:
            s: given string

        Returns:
            True if the string is palindrome, else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """


        result = ""

        for char in s:

            if not char.isalnum():
                continue

            result += char.lower()

        return result == result[::-1]

s = Solution()
assert s.validPalindrome(s = "Was it a car or a cat I saw?") == True
assert s.validPalindrome(s = "tab a cat") == False
assert s.validPalindrome(s = "") == True
print("passed")

# 11.41 -> 9 min