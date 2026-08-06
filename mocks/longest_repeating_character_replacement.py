class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Find length of longest substring which contains only one character with k replacements.

        Args:
            s: input string
            k: allowed number of replacement characters

        Returns:
            length of longest substring with k replacements

        Time: O(n) - n = len(s)
        Space: O(1)
        """
        longest = 0
        left = 0
        count = [0] * 26
        max_char_count = 0

        for right in range(len(s)):
            curr_char_index  = ord(s[right]) - ord("A")
            count[curr_char_index] += 1
            max_char_count = max(max_char_count, count[curr_char_index])

            # new character has been added to its index, count has been increased for it and also kept tap of max repeated character.
            # now i have right index, left index.
            # and its time to check length of current window and subtract max repeated character count from it
            # if its greater than k, means we have added unnecessary character in our substring window.
            # thats why remove left character and move left by 1. this way window length stayed same.
            # now check for length of substring -> compare (right - left + 1) current window length to longest = 0
            # return longest

            if (right - left + 1) - max_char_count > k:         # added more than permitted
                count[left] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest

s = Solution()
assert s.characterReplacement(s = "XYYX", k = 2) == 4
assert s.characterReplacement(s = "AAABABB", k = 1) == 5
assert s.characterReplacement(s="ABCDEF", k =1) == 2
print("passed")