# 1.32

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Find out if the given strings are angram or not.

        Args:
            s, t (str): given strings

        Returns:
            bool: True if both are anagrams else False

        Time: O(n) - n = len(s)
        Space: O(1)
        """

        if len(s) != len(t):
            return False

        count_s = [0] * 26
        count_t = [0] * 26

        for index in range(len(s)):
            count_s[ord(s[index]) - ord("a")] += 1
            count_t[ord(t[index]) - ord("a")] += 1

        return count_s == count_t

s = Solution()
assert s.isAnagram("anagram", "nagaram") == True
assert s.isAnagram("rat", "car") == False
assert s.isAnagram("", "") == True
assert s.isAnagram("a", "ab") == False
assert s.isAnagram("aacc", "ccac") == False
print("passed")