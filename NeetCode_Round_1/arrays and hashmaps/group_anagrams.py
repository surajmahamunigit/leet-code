from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Args:
            list[str] : List of strings

        Returns:
            list[list[str]] : Group of anagrams

        Time: O(n*k)    # n= number of words, k= avg word length
        Space: O(n*k)
        """

        result = defaultdict(list)

        # Group of words -> word -> char count
        for word in strs:

            char_count = [0] * 26
            for ch in word:

                ch_index = ord(ch) - ord("a")
                char_count[ch_index] += 1

            result[tuple(char_count)].append(word)

        return list(result.values())


result = Solution().groupAnagrams(["cat", "act", "dog"])
print(result)