class Solution:
    def longestRepeatingCharacter(self, s: str, k: int) -> int:
        """
        Args:
            s: input string
            k: max replacement allowed

        Returns:
            length of longest substring with same letter after k replacements

        Time: O(n) - n = len(s)
        Space: O(1)
        """

        longest = 0
        left = 0
        max_ch_freq = 0
        counts = [0] * 26

        for right in range(len(s)):
            # Character index
            char_index = ord(s[right]) - ord("A")

            # Increase character count by 1
            counts[char_index] += 1

            # Update its max frequency
            max_ch_freq = max(max_ch_freq, counts[char_index])

            # if window is invalid - remove left char
            # current window length -> (right - left + 1)
            # invalid window -> if (current_window_length - max_ch_freq) > k
            if (right - left + 1) - max_ch_freq > k:

                # Remove left
                counts[ord(s[left]) - ord("A")] -= 1
                left += 1

            longest = max (longest, (right - left + 1))     # here (right - left + 1) is new window length, after removing s[left]


        return longest

result = Solution().longestRepeatingCharacter(s="AABABC", k= 0)
print(result)
