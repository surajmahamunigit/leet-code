"""
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        left_index = 0
        result = 0

        for right_index in range(len(s)):

            # If the char is present in char_set
            while s[right_index] in char_set:
                char_set.remove(s[left_index])
                left_index += 1

            # If the char is not present in the char_set
            char_set.add(s[right_index])
            result = max(result, right_index-left_index+1)

        return result


result = Solution().lengthOfLongestSubstring("abcabcbb")
print(result)

