# 9.19

class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        """Find the longest length of substring with k character replacements.

        Args:
            s (str): given string
            k (int): number of character replacements allowed

        Returns:
            int: longest length  of substring with k character replacements

        Time complexity: O(n) - n = len(s)

        Space complexity: O(1)
        """

        # s = "ABCAS", k= 2 -> 4

        count = [0] * 26
        longest = 0
        max_char_freq = 0
        left = 0

        for index in range(len(s)):
            char_index = ord(s[index]) - ord("A")
            count[char_index] += 1
            max_char_freq = max(max_char_freq, count[char_index])

            if (index - left + 1) - max_char_freq > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            longest = max(longest, index - left + 1)
        return longest

s = Solution()
print(s.character_replacement("ABCAS", 1))
