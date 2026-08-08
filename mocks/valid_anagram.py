# algorithm
# given two strings s and t.
# do the character freq count for both strings and then compare


class Solution:
    def valid_anagram(self, s: str, t: str) -> bool:
        """Find if two strings are anagram of each other.

        Args:
            s: first string
            t: second string

        Returns:
            True if both strings are anagram, else False

        Time: O(n) - len(s)
        Space: O(n)
        """

        # if lengths are not same
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}
        for index in range(len(s)):
            count_s[s[index]] = count_s.get(s[index], 0) + 1
            count_t[t[index]] = count_t.get(t[index], 0) + 1

        return count_s == count_t

s = Solution()
#res = s.valid_anagram(s = "racecar", t = "carrace")
res = s.valid_anagram(s = "jar", t = "jam")
print(res)


