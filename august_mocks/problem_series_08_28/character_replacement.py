# 2.49

class Solution:
    def characterReplacement(self,s: str, k: int) -> int:
        """Find longest length possible of substring with single unique character with k replacements.

        Args:
            s: given string
            k: number of character replacements allowed

        Returns:
            length of longest substring with single unique character with k replacements

        Time: O(n) - n = len(s)
        Space: O(1)
        """
        longest = 0
        count = {}
        left = 0
        max_count = 0
        for index in range(len(s)):
            char = s[index]

            count[char] = count.get(char, 0) + 1
            max_count = max(max_count, count[char])
            curr_len = index - left + 1
            if curr_len - max_count > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, index - left + 1)

        return longest

s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("", 0) == 0
assert s.characterReplacement("AAAA", 0) == 4
assert s.characterReplacement("A", 0) == 1
print('passed')

# 2.59 -> 10 min to solve