# 7.04

class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        """Return length of longest sub string.

        Args:
            s: given string

        Returns:
            length of longest sub string without repeating character

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        # s = "abcabcbb"

        longest = 0
        left = 0
        seen = set() # abc

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            curr_len = right - left + 1
            longest = max(longest, curr_len)

        return longest


s = Solution()
assert s.length_of_longest_substring("abcabcbb") == 3   # classic case
assert s.length_of_longest_substring("bbbbb") == 1        # all same char
assert s.length_of_longest_substring("") == 0             # empty string
assert s.length_of_longest_substring("a") == 1            # single char
assert s.length_of_longest_substring("abba") == 2         # double-shrink case (tripped you up this morning)
assert s.length_of_longest_substring("pwwkew") == 3       # repeat appears mid-string
print("passed")

# 7.17 -> 13 min to finish