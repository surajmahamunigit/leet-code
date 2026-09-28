# 1.05

class Solution:
    def longest_substring(self, s: str) -> int:
        """Find the length of longest substring without repeating characters.

        Args:
            s (str): given string

        Returns:
            int: length of longest substring without repeating characters

        Time: O(n) - n = len(s)

        Space: O(n)
        """

        # s = "zxyzxyz"

        left = 0
        seen = set()
        longest = 0
        for index in range(len(s)):
            char = s[index]

            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            curr_length = index - left + 1
            longest = max(longest, curr_length)

        return longest

s = Solution()
print(s.longest_substring("abcabcbb"))
print(s.longest_substring("bbbb"))
print(s.longest_substring(""))