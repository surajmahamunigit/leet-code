# 10.51
from collections import defaultdict


class Solution:
    def group_anagram(self, strs: list[str]) -> list[list[str]]:
        """Group the given list of words in the as anagrams.

        Args:
            strs (list[str]): list of strings

        Returns:
             lis[list[str]]: list of group of anagrams

        Time: O(n) - n = total number of characters in strs

        Space: O(n)
        """
        result = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(word)

        return list(result.values())