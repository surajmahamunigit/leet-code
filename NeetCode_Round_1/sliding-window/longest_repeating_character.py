class Solution:
    def longestRepeatingCharacter(self, s: str, k: int) -> int:
        """

        """
        longest = 0
        left = 0
        max_char_count = 0
        counts= [0] * 26

        for right in range(len(s)):

            # Char index
            char_index = ord(s[right]) - ord("A")

            counts[char_index] += 1

            max_char_count = max(max_char_count, counts[char_index])

            if (right - left + 1) - max_char_count > k:
                counts[left] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest

result = Solution().longestRepeatingCharacter(s="AABAC", k=0 )
print(result)