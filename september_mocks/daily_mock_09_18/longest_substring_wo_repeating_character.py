# 9.52

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find the length of longest substring without repeating character.

        Args:
            s (str): given string

        Returns:
            int: length of the longest substring without repeating any character

        Time: O(n) - n = len(s)

        Space: O(n)
        """

        # s = "zxyzxyz"

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
print(s.lengthOfLongestSubstring("zxyzxyz"))
print(s.lengthOfLongestSubstring("xxxx"))

# 9.58 -> 6 min