# 6.27

class Solution:
    def longest_substring(self, s: str) -> int:
        """Find the longest substring without repeating characters.

        Args:
            s (str): given string

        Returns:
            int: length of longest substring without repeating characters

        Time complexity: O(n) - n = len(s)

        Space complexity: O(n)
        """

        longest = 0
        left = 0
        seen = set()

        for index in range(len(s)):
            char = s[index]

            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            length = index - left + 1
            longest = max(longest, length)

        return longest

s = Solution()

def check(values, expected):
    result = s.longest_substring(values)
    assert result == expected

check("zxyzxy", 3)
check("", 0)
check("a", 1)
check("ab", 2)
check("aabbcc", 2)
print("all tests passed")
