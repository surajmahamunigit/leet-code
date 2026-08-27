# 1.01
# given a string and asked to find out length of longest substring without repeating char

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find the length of longest substring without repeating characters.

        Args:
            s: input string

        Returns:
            length of longest substring without repeating characters

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        seen = set()
        left = 0
        longest = 0

        for index in range(len(s)):

            char = s[index]

            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            curr_len = index - left + 1
            longest = max(longest, index - left + 1)

        return longest

s = Solution()
assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbbbb") == 1
assert s.lengthOfLongestSubstring("") == 0
assert s.lengthOfLongestSubstring("a") == 1
assert s.lengthOfLongestSubstring("abba") == 2
assert s.lengthOfLongestSubstring("pwwkew") == 3
print("passed")

# 1.09 -> 8 min to solve