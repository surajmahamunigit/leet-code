# 9.54

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Find out if given string is palindrome or not.

        Args:
            s: given string

        Returns:
            True if string is palindrome else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        res = ""

        for index in range(len(s)):
            if self.isAlphaNum(s[index]):
                res += s[index].lower()

        return res == res[::-1]

    def isAlphaNum(self, c: str):

        return ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9")

s = Solution()
assert s.isPalindrome("A man, a plan, a canal: Panama") == True
assert s.isPalindrome("race a car") == False
assert s.isPalindrome(" ") == True
assert s.isPalindrome(".,") == True
assert s.isPalindrome("0P") == False
print("passed")

# 10.05 -> 10 min to finish