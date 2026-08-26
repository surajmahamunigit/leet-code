# 8.32

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Find and group anagram strings into sublists and return list.

        Args:
            strs: list of strings

        Returns:
            list of sublists of grouped anagrams

        Time: O(n) - total characters in strs
        Space: O(n)
        """
        group = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                char_index = ord(char) - ord("a")
                count[char_index] += 1

            group[tuple(count)].append(word)

        return list(group.values())

s = Solution()
res = s.groupAnagrams(strs = [""])
print(res)

# 8.43 -> 11 min to solve