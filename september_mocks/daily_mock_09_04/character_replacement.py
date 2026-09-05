# 9.03

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Find the length of longest substring with one character and k replacements.

        Args:
            s: given string
            k: number of replacements allowed

        Returns:
            int: length of longest substring with one character and k replacements

        Time: O(n) - n = len(s)
        Space: O(1)
        """
        longest = 0

        count = [0] * 26
        left = 0
        max_count = 0

        for index in range(len(s)):
            char_index = ord(s[index]) - ord("A")

            count[char_index] += 1
            max_count = max(max_count, count[char_index])
            curr_len = index - left + 1

            if curr_len - max_count > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            longest = max(longest, index - left + 1)

        return longest

s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("", 0) == 0
assert s.characterReplacement("AAAA", 0) == 4
assert s.characterReplacement("A", 0) == 1
print('passed')