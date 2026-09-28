# 1.16

class Solution:
    def longest_repeating_character(self, s: str, k: int) -> int:
        """Find the length of longest substring with distinct character and with k replacements.

        Args:
            s (str): given input string with uppercase characters.
            k (int): max allowed number of replacements.
        Returns:
            int: length of longest substring with distinct character and with allowed k replacements.

        Time: O(n) - n = len(s)

        Space: O(1)
        """

        # s = "XYYX", k = 2

        count = [0] * 26
        longest = 0
        left = 0
        max_count = 0
        for index in range(len(s)):
            char = ord(s[index]) - ord("A")
            count[char] += 1
            max_count = max(max_count, count[char])

            if (index - left + 1) - max_count > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            curr_window = index - left + 1
            longest = max(longest, curr_window)

        return longest

s = Solution()
print(s.longest_repeating_character("XYYX", 2))
print(s.longest_repeating_character("AAABABB", 1))
print(s.longest_repeating_character("", 2))