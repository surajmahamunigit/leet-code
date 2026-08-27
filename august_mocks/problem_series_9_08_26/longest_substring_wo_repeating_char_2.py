# 9.42

class Solution:
    def lengthOfLongestSubString(self, s: str) -> int:
        """Find length of longest substring without repeating character.

        Args:
            s: given string

        Returns:
            length of longest substring without repeating char

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        # s = "zxyzxyz"
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
res = s.lengthOfLongestSubString("xxxx")
print(res)

# 9.50 -> 8 min to solve