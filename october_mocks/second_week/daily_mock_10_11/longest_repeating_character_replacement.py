# 8.32

# given -> string with uppercase letters
# you can replace k characters
# return -> length of longest substring with same characters

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Find the length of the longest substring with same characters and k replacements.

        Args:
            s (str): given string with uppercase letters
            k (int): number of allowed replacements
        Returns:
            int: length of the longest substring with same characters with k replacements

        Time complexity: O(n) - n = len(s)

        Space complexity: O(1)
        """

        left = 0
        max_count = 0
        count = [0] * 26
        longest = 0

        for index in range(len(s)):
            char_index = ord(s[index]) - ord("A")
            count[char_index] += 1

            max_count = max(max_count, count[char_index])
            curr_len = index - left + 1
            if curr_len - max_count > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            longest = max(longest, index - left + 1)

        return longest

# 8.51 -> 19 minutes to solve problem
# git commit -> feat: add longest repeating character replacement solution

s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("AAAA", 2) == 4
assert s.characterReplacement("A", 0) == 1
assert s.characterReplacement("A", 1) == 1
assert s.characterReplacement("ABC", 0) == 1
assert s.characterReplacement("ABC", 1) == 2
assert s.characterReplacement("ABC", 2) == 3
assert s.characterReplacement("ABC", 3) == 3
assert s.characterReplacement("AABBB", 0) == 3
assert s.characterReplacement("ABBB", 2) == 4
assert s.characterReplacement("BAAAB", 2) == 5
assert s.characterReplacement("ABAA", 0) == 2
assert s.characterReplacement("ABCDE", 2) == 3
assert s.characterReplacement("AABABBA", 2) == 5
assert s.characterReplacement("A" * 50000 + "B" * 50000, 0) == 50000
assert s.characterReplacement("AB" * 50000, 50000) == 100000
assert s.characterReplacement("AB" * 50000, 25000) == 50001
