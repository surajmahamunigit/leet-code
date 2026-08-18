# 12.19
# given string, asked to find if the given string is palindrome
# check if character is alpha numeric and then add to res -> compare result

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Find out if given string is palindrome or not.

        Args:
            s: given string

        Returns:
            True if string is palindrome, else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """
        res = ""

        for char in s:
            if char.isalnum():
                res += char.lower()

        return res == res[::-1]

s = Solution()
assert s.isPalindrome("A man, a plan, a canal: Panama") == True
assert s.isPalindrome("race a car") == False
assert s.isPalindrome(" ") == True
assert s.isPalindrome(".,") == True
assert s.isPalindrome("0P") == False
print('passed')

# 12.24 -> 5 min to finish