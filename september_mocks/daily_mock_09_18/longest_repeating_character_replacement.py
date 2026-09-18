# 10.01

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Length of the longest substring with k replacements.

        Args:
            s (str): given string with uppercase letters
            k (int): number of replacements allowed

        Returns:
            int: length of longest substring with k replacements

        Time: O(n) - n = len(s)

        Space: O()
        """

        # Input: s = "XYYX", k = 2

        longest = 0
        max_count = 0
        left = 0
        count = [0] * 26

        for index in range(len(s)):
            char = s[index]
            char_index = ord(char) - ord("A")
            count[char_index] += 1
            max_count = max(max_count, count[char_index])

            if (index - left + 1) - max_count > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            longest = max(longest, index - left + 1)

        return longest

s = Solution()
print(s.characterReplacement(s = "XYYX", k = 2))
print(s.characterReplacement(s = "AAABABB", k = 1))

