# algorithm
# given list of strings and asked to find out sublists of group of anagrams
# for each word in strs array -> count char freq in [0] * 26 array
# typecast it to tuple and use that array as key while adding to the result dict
# in end return values of result dict.

from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        """Group anagrams strings together in sublists and return all sublist.

        Args:
            strs: lists of strings

        Returns:
            list containing group of sublists containing anagrams.

        Time: O(n * m) - n = len(strs), m = average length of each word
        Space: O(m*n)
        """

        if not strs:
            return []

        result = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_index = ord(char) - ord("a")
                char_count[char_index] += 1

            result[tuple(char_count)].append(word)

        return list(result.values())

s = Solution()
#res = s.group_anagrams(strs = ["act","pots","tops","cat","stop","hat"])
#res = s.group_anagrams(strs = [""])
res = s.group_anagrams(strs = ["x"])
print(res)