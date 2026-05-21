"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Method 1: Using isalnum()
        #
        # new_string = ""
        #
        # for ch in s:
        #
        #     if ch.isalnum():
        #         new_string +=ch.lower()
        #
        # return new_string == new_string[::-1]


        # Method 2:

        left, right = 0, len(s) - 1

        while left < right:
            # if s[left] is not alpha-numeric, move to next index
            while (left < right) and not (self.alphaNum(s[left])):
                    left += 1
            # if s[right] is not alpha-numeric, move to next character (backward index)
            while (right > left) and not (self.alphaNum(s[right])):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left, right = left + 1, right - 1

        return True


    def alphaNum(self, ch):

        return (ord("A") <= ord(ch) <= ord("Z") or ord("a") <= ord(ch) <= ord("z") or ord("0") <= ord(ch) <= ord("9"))



print(Solution().isPalindrome("A man, a plan, a canal: Panama"))