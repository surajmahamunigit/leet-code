# 3.05
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Find and group anagram strings.

        Args:
            strs: list of given strings

        Returns:
            list containing sublists of anagrams

        Time: O(n) - n = total characters in strs
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
print("passed")

# 3.12 -> 7 min to solve