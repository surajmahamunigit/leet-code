# 5.17

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find length of longest substring without repeating any character.

        Args:
            s: given string

        Returns:
            int: length of longest substring without repeating any character

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        longest = 0
        left = 0
        seen = set()
        for index in range(len(s)):

            while s[index] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[index])
            curr_len = index - left + 1
            longest = max(longest, curr_len)

        return longest

s = Solution()
assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbbbb") == 1
assert s.lengthOfLongestSubstring("") == 0
assert s.lengthOfLongestSubstring("a") == 1
assert s.lengthOfLongestSubstring("abba") == 2
assert s.lengthOfLongestSubstring("pwwkew") == 3
print("passed")

# 5.27