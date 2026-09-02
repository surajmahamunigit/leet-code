# 11.41

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find the length of the longest substring without repeating characters.

        Args:
            s: given string

        Returns:
            the length of the longest substring without repeating characters

        Time: O(n) - n = len(s)
        Space: O(n)
        """
        longest = 0

        seen = set()
        left = 0

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
print("passed")

# 11.50 -> 9 min