# 9.20
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Find and group all anagram strings in sublists and return list.

        Args:
            strs (list[str]): list of anagram strings

        Returns:
            list[list[str]]: list of group anagram strings

        Time: O(n) - n = total number of characters in given strs
        Space: O(n)
        """

        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1

            result[tuple(count)].append(word)

        return list(result.values())

s = Solution()
def normalize(result):
    return sorted(sorted(group) for group in result)

assert normalize(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) == normalize([["bat"],["nat","tan"],["ate","eat","tea"]])
assert s.groupAnagrams([""]) == [[""]]
assert s.groupAnagrams(["a"]) == [["a"]]
print('passed')