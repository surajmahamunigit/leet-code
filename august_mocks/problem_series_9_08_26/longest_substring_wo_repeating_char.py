# 12.38

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find the length of longest substring without repeating character.

        Args:
            s: given string

        Returns:
            length of longest substring without repeating character

        Time:
        Space:
        """
        longest = 0
        seen = set()
        left = 0
        for index in range(len(s)):
            char = s[index]

            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            curr_len = index - left + 1
            longest = max(longest, curr_len)

        return longest

s= Solution()
res = s.lengthOfLongestSubstring("zxyzxyz")
print(res)

# 12.55