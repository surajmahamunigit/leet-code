# 11.45
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Return group anagrams strings as sublists.

        Args:
            strs: lists of strings

        Returns:
            list containing sublists of anagram strings

        Time: O(p) - p = total characters in strs
        Space: O(p)

        """

        # ["eat","tea","tan","ate","nat","bat"]

        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(word)

        return list(res.values())

s = Solution()

def normalize(result):
    return sorted(sorted(group) for group in result)

assert normalize(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) == normalize([["bat"],["nat","tan"],["ate","eat","tea"]])
assert s.groupAnagrams([""]) == [[""]]
assert s.groupAnagrams(["a"]) == [["a"]]
print("passed")

# 11.53 -> 8 min to finish
