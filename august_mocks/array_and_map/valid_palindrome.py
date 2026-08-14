# 5.54

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Find out if given string is palindrome or not.

        Args:
            s: input string

        Returns:
            True if string is palindrome, else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """
        if s == "":
            return True

        res = ""
        for char in s:
            if not char.isalnum():
                continue

            res += char.lower()

        return res == res[::-1]

s = Solution()
assert s.isPalindrome("A man, a plan, a canal: Panama") == True
assert s.isPalindrome("race a car") == False
assert s.isPalindrome(" ") == True
assert s.isPalindrome(".,") == True
assert s.isPalindrome("0P") == False
print("passed")

# 5.58 -> 4 minute to solve