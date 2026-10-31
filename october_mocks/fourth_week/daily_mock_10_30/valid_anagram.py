# 10.02

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        """Find out if the given strings are anagrams of each other.

        Args:
            s, t (str): given strings

        Returns:
            bool: True if the s and t are anagrams of each other, else False

        Time complexity: O(n) - n = total number of characters in string s

        Space complexity: O(1)
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

def check(values1, values2, expected):
    result = s.is_anagram(values1, values2)
    assert result == expected

check("", "", True)
check("ab", "", False)
check("ab", "cd", False)
check("racecar", "carrace", True)
print("all passed")