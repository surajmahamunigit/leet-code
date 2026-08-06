# algorithm
# given s = "XYYXA", k = 2
# we have been told all character will be uppercase characters, thats a hind for [0] * 26
# lets start with longest = 0, max_char_count = 0, left = 0 and char_count = [0] * 26
# for index in range(len(s)):
# find char_index = ord(char) - ord("A") and increase by 1 at count array
# now find max_char_freq = max(max_char_freq, count[char_index]), this will give us running count of frequently repeated character
# now find length of current substring = index - left + 1
# if current_length - max_char_freq > k means we have used more than k replacements and time to drop char at left from count and move left
# this way window size stays same. now compare with longest to keep track of longest length of substring with k replacements.
# in end return longest


# example
# for i = 0, s[0]=char = X, index = ord(char) - ord("A") = 24, count[25] += 1, max_char_count = max(max_char_count, count[25])=1, k= 0 longest = 1
# for i = 1, s[1]=char = Y, index = ord(char) - ord("A") = 25, count[25] += 1, max_char_count = max(max_char_count, count[25])=1, k= 1 longest = 2
# for i = 2, s[0]=char = Y, index = ord(char) - ord("A") = 25, count[25] += 1 -> 2, max_char_count = max(max_char_count, count[25])=2, k= 1 longest = 3
# for i = 3, s[0]=char = X, index = ord(char) - ord("A") = 24, count[24] += 1 -> 2, max_char_count = max(max_char_count, count[25])=2, k= 2 longest = 4
# for i = 4, s[0]=char = A, index = ord(char) - ord("A") = 0, count[0] += 1, max_char_count = max(max_char_count, count[25])=2, k= 3 -> remove left, count[ord(s[left])] -= 1, left = 1, longest = 4
# longest = 4

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Find length of longest substring which contains unique characters with k replacements.

        Args:
            s: input string
            k: number of character replacements allowed

        Returns:
              length of longest substring which contains unique characters with k replacements

        Time: O(n) - n = len(s)
        Space: O(1)
        """

        longest = 0         # to keep tab of length of longest substring

        max_char_count = 0  # maximum occur character
        left = 0
        count = [0] * 26    # to keep count of 26 characters

        for index in range(len(s)):
            char_index = ord(s[index]) - ord("A")
            count[char_index] += 1
            max_char_count = max(max_char_count, count[char_index])     # keeps tab of max occurred char

            # if we just added char that increased k than given limits. means its invalid, thats why remove left char, this we we keep window same size despite having more k
            if (index - left + 1) - max_char_count > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            # now window size stayed same despite being wrong.
            longest = max(longest, index - left + 1)        # index - left + 1 -> still has right window length

        return longest


s = Solution()
assert s.characterReplacement(s = "XYYX", k = 2) == 4
assert s.characterReplacement(s = "AAABABB", k = 1) == 5
assert s.characterReplacement(s = "ABCDEF", k = 1) == 2
print("passed")