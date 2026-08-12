# 12.27
class Solution:
    def encode(self, strs: list) -> str:
        """Encode given list of strings and return single string.

        Args:
            strs: list of strings

        Returns:
            encoded string

        Time: O(m) - total characters
        Space: O(m)
        """
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word

        return res


    def decode(self, s: str) -> list[str]:
        """Decode the given string and return original list of strings.

        Args:
            s: encoded string

        Returns:
            list of all words after decoding string

        Time:
        Space:
        """
        res = []
        left = 0
        while left < len(s):

            index = left

            while s[index] != "#":
                index += 1

            word_len = int(s[left : index])      # this will give us word length
            word = s[index + 1 : index + 1 + word_len]
            res.append(word)

            left = index + 1 + word_len

        return res

s = Solution()
res = s.decode(s.encode(strs = ["Hello","World"]))
print(res)