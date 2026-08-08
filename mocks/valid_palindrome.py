# algorithm
# given string and asked to find out if its palindrome or not
# assume res = "", for every char in s, check if its alph numeric or not, if yes add it to string, else skip
# in end compare string and string backward

class Solution:
    def valid_palindrome(self, s: str) -> bool:
        """Find out if given string is palindrome or not.

        Args:
            s: input string

        Returns:
            True if string is palindrome else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        res = ""
        for index in range(len(s)):
            if not s[index].isalnum():
                continue

            res += s[index].lower()

        return res == res[::-1]

s = Solution()
res = s.valid_palindrome(s = "Was it a car or a cat I saw?")
print(res)