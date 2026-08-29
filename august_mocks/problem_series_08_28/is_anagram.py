# 8.15
from sqlalchemy.testing.util import count_cache_key_tuples


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Find out if given two strings are anagram of each other.

        Args:
            s, t: given strings

        Returns:
            True if the strings are anagram of each other, else False

        Time: O(n) - n = len(s)
        Space: O(1)
        """

        if len(s) != len(t):
            return False

        # character count for both words
        count_s = [0] * 26
        count_t = [0] * 26

        for index in range(len(s)):
            count_t[ord(t[index]) - ord("a")] += 1
            count_s[ord(s[index]) - ord("a")] += 1

        return count_t == count_s

s = Solution()
assert s.isAnagram("anagram", "nagaram") == True
assert s.isAnagram("rat", "car") == False
assert s.isAnagram("", "") == True
assert s.isAnagram("a", "ab") == False
assert s.isAnagram("aacc", "ccac") == False
print("passed")