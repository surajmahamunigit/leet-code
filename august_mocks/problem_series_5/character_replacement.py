# 3.11
# given string s and asked to find length of longest substring with k possible replacements.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Find the length of longest substring without repeating character with k replacements.

        Args:
            s: given string

        Returns:
            length of longest substring without repeating character with k replacements

        Time: O(n) - n = len(s)
        Space: O(1)
        """

        left = 0
        right = 0
        count = [0] * 26
        max_char_count = 0
        longest = 0

        while right < len(s):
            char_index = ord(s[right]) - ord("A")
            count[char_index] += 1

            max_char_count = max(max_char_count, count[char_index])
            curr_len = right - left + 1

            if curr_len - max_char_count > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            longest = max(longest , right - left + 1)
            right += 1

        return longest

s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("", 0) == 0
assert s.characterReplacement("AAAA", 0) == 4
assert s.characterReplacement("A", 0) == 1
print("passed")

# 3.25 -> 14 min to solve
# add it to repetition for tomorrow