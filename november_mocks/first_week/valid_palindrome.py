# 11.21

class Solution:
    def valid_palindrome(self, s: str) -> bool:
        """Find the given string is palindrome or not.

        Args:
            s (str): given string

        Returns:
            bool: True if the given string is palindrome else False

        Time complexity: O(n) - n = len(s)

        Space complexity: O(1)
        """

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

s = Solution()

def check(values, expected):
    result = s.valid_palindrome(values)
    assert result == expected

check("was it a car or a cat i saw?", True)
check("aa", True)
check("tab a cat", False)
check("", True)
check("Aa", True)
check(",./", True)
check("a.", True)
print("all tests passed")

# 11.29 -> 8 minutes to solve the problem
# git commit -> feat: add valid palindrome solution