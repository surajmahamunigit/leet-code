# 1.49
# given string s and asked to find out length of longest substring with one distinct char and k replacements

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Find the length of longest substring with one distinct character and k replacements.

        Args:
            s: given string with only uppercase letters
            k: number of allowed replacements

        Returns:
            length of longest substring with one distinct character and k replacements

        Time: O(n) - n = len(s)
        Space: O(1)
        """
        count = [0] * 26
        left = 0
        max_char_count = 0
        longest = 0

        for index in range(len(s)):
            char = s[index]
            char_index = ord(char) - ord("A")
            count[char_index] += 1
            max_char_count = max(max_char_count, count[char_index])

            curr_len = index - left + 1
            if curr_len - max_char_count > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            longest = max(longest, index - left + 1)

        return longest


# 2 -> 12 min to solve