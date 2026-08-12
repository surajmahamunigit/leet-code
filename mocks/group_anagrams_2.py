from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        """Group anagrams together in sub-lists and return.

        Args:
            strs: list of string, anagrams

        Returns:
            sub-lists with grouped anagrams

        Time: O(m*n)
        Space: O(m*n)
        """

        seen = defaultdict(list)

        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord("a")] += 1

            seen[tuple(char_count)].append(word)

        return list(seen.values())

s = Solution()
res = s.group_anagrams(strs = ["act","pots","tops","cat","stop","hat"])
print(res)