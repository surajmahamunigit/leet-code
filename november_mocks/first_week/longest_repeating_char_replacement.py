# 6.49

class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        """Find length of longest substring with k replacement characters.

        Args:
            s (str): given string with uppercase letters
            k (int): number of character replacements allowed

        Returns:
             int: length of longest substring with k replacement characters

        Time complexity: O(n) - n = len(s)

        Space complexity: O(1)
        """

        longest = 0
        count = [0] * 26
        max_char_freq = 0
        left = 0

        for index, char in enumerate(s):
            char_index = ord(char) - ord("A")
            count[char_index] += 1
            max_char_freq = max(max_char_freq, count[char_index])

            if (index - left + 1) - max_char_freq > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            longest = max(longest, index - left + 1)

        return longest

s = Solution()

def check(values, k, expected):
    result = s.character_replacement(values, k)
    assert result == expected

check("", 0, 0)
check("A", 0, 1)
check("AB", 0, 1)
check("AB", 1, 2)
check("ABCD", 2, 3)
check("AABC", 1, 3)
check("ABAB", 2, 4)
check("AAABAA", 1, 6)

print("all tests passed")