# 9.20

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        """Find if the given strings are anagram of each other.

        Args:
            s, t (str): given strings

        Returns:
            bool: True if strings are anagram else False

        Time: O(n) - n = len(s)

        Space: O(n)
        """

        if len(s) != len(t):
            return False

        count_s = [0] * 26
        count_t = [0] * 26

        for index in range(len(s)):
            count_s[ord(s[index]) - ord("a")] += 1
            count_t[ord(t[index]) - ord("a")] += 1

        return count_s == count_t