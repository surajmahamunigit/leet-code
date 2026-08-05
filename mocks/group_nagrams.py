# Algorith:
# array of strings is given and we need to group anagrams strings into sublist.
# for each string in array, and count the character frequency and use char_freq = [1] * 26, for 26 characters
# check if it exists in group dict. if it does, add it to the dict at char_freq. char_freq -> [word]
# if it doesnt, add it add as tuple(char_freq) -> [word]
# in the end return values from result array that contains all keys and sublists



# Example
# strs = ["act","pots","tops","cat","stop","hat"]
# result = [], char_freq=[1]*26
# i=0 -> result[(char_freq1):[act]]
# i=1 -> result = [(char_freq1):[act], (char_freq2):[pots]]
# i=2 -> result = [(char_freq1):[act], (char_freq2):[pots,tops]]
# i=3 -> result = [(char_freq1):[act,cat], (char_freq2):[pots,tops],]
# i=4 -> result = [(char_freq1):[act,cat], (char_freq2):[pots,tops,stop],]
# i=5 -> result = [(char_freq1):[act,cat,](char_freq3):[hat], (char_freq2):[pots,tops,stop],]

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Group list of anagram strings together in sublist

        Args:
            strs: list of strings

        Returns:
            list of sublist containing anagram strings

        Time: O(m*n) - n = len(strs), m = average length of word
        Space: O(m*n))
        """

        result = defaultdict(list)

        for word in strs:
            char_freq = [0] * 26
            for char in word:
                char_freq[ord(char) - ord("a")] += 1    # just add 1

            result[tuple(char_freq)].append(word)

        return list(result.values())

s = Solution()
assert s.groupAnagrams(["act","pots","tops","cat","stop","hat"]) == [["act", "cat"],["pots","tops","stop"],["hat"]]
assert s.groupAnagrams(["x"]) == [["x"]]
assert s.groupAnagrams([""]) == [[""]]
print("passed")
