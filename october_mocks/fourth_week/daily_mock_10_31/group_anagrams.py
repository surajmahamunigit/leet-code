# 8.44

from collections import defaultdict
class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        """Group the given list of strings into a list of all possible Anagrams.

        Args:
            strs (list[str]): list of strings

        Returns:
            list[list[str]]: list of anagrams

        Time complexity: O(n) - n = total number of characters in given list

        Space complexity: O(n)
        """
        anagrams = defaultdict(list)


        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1

            anagrams[tuple(count)].append(word)

        return list(anagrams.values())

s = Solution()

def normalize(groups):
    return sorted(sorted(group) for group in groups)

def check(values, expected):
    result = s.group_anagrams(values)
    assert normalize(result) == normalize(expected)

check( ["act","pots","tops","cat","stop","hat"], [["hat"],["act", "cat"],["stop", "pots", "tops"]] )
check(["x"], [["x"]])
check([""], [[""]])
print("all passed")

# 9.10
# git commit -> feat: add group anagrams solution