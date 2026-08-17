# 2.31

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find the length of longest substring in given string without repeating characters.

        Args:
            s: given string

        Returns:
            length of longest substring in given string without repeating characters

        Time: O(n) - n = len(s)
        Space: O(n)
        """
        seen = set ()

        left = 0
        right = 0
        longest = 0

        while right < len(s):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            curr_len = right - left + 1
            longest = max(curr_len, longest)
            right += 1

        return longest

s = Solution()
assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbbbb") == 1
assert s.lengthOfLongestSubstring("") == 0
assert s.lengthOfLongestSubstring("a") == 1
assert s.lengthOfLongestSubstring("abba") == 2
assert s.lengthOfLongestSubstring("pwwkew") == 3
print("passed")

# 2.39 -> 8 min to solve