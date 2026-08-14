# 10.52

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Find out if given string s and t are anagrams or not.

        Args:
            s, t: given strings

        Returns:
            True if given strings are anagrams else False

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for index in range(len(s)):
            s_count[s[index]] = s_count.get(s[index], 0) + 1
            t_count[t[index]] = t_count.get(t[index], 0) + 1

        return s_count == t_count

s = Solution()
assert s.isAnagram("anagram", "nagaram") == True
assert s.isAnagram("rat", "car") == False
assert s.isAnagram("", "") == True
assert s.isAnagram("a", "ab") == False
assert s.isAnagram("aacc", "ccac") == False
print("passed")

# 10.56 -> 4 minutes to solve