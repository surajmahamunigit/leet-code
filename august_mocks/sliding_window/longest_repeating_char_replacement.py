# 10.56

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Find length of longest sub string with k replacements.

        Args:
            s: given string with uppercase characters
            k: number of replacements allowed

        Returns:
            length of longest sub string with k replacements

        Time: O(n) - n = len(s)
        Space: O(1) - only 26 uppercase letters at max
        """

        # s = "ABAB", k = 2
        longest = 0

        left = 0
        right = 0
        count = {}
        max_char_freq = 0

        while right < len(s):

            # count freq of each char
            count[s[right]] = count.get(s[right], 0) + 1

            max_char_freq = max(max_char_freq, count[s[right]])
            curr_length = right - left + 1
            if curr_length - max_char_freq > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            right += 1

        return longest

s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("", 0) == 0
assert s.characterReplacement("AAAA", 0) == 4
assert s.characterReplacement("A", 0) == 1
print("passed")

# 11.14 -> 18 minute sto finish