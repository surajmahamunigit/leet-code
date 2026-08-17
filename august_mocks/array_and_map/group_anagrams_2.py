# 12.58
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Group all the anagram strings together in sublist and return a list.

        Args:
            strs: list of strings

        Returns:
            groups anagram strings together and returns a list

        Time: O(n) - n = total character count in strs
        Space: O(n)
        """
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                char_index = ord(char) - ord("a")
                count[char_index] += 1

            res[tuple(count)].append(word)

        return list(res.values())

s = Solution()
def normalize(result):
    return sorted(sorted(group) for group in result)

assert normalize(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) == normalize([["bat"],["nat","tan"],["ate","eat","tea"]])
assert s.groupAnagrams([""]) == [[""]]
assert s.groupAnagrams(["a"]) == [["a"]]

print("passed")

# 1.06 -> 8 min to solve
