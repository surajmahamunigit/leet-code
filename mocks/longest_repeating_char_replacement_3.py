# algorithm
# given string with repeated characters and we have to find the length of longest substring with k replacements


class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        """Find length of longest substring with containing distinct character with k replacements.

        Args:
            s: input string
            k: number of replacements available

        Returns:
            length of longest substring with k replacements

        Time: O(n) - n = len(s)
        Space: O(1)
        """

        longest = 0

        char_count = [0] * 26
        left = 0
        max_char_freq = 0

        for index in range(len(s)):

            char = s[index]
            char_count[ord(char) - ord("A")] += 1
            max_char_freq = max(max_char_freq, char_count[ord(char) - ord("A")])
            curr_len = index - left + 1

            if curr_len - max_char_freq  > k:
                char_count[ord(s[left]) - ord("A")] -= 1
                left += 1

            longest = max(longest, index - left + 1)

        return longest

s = Solution()
res = s.character_replacement("XYYX", 2)
print(res)



