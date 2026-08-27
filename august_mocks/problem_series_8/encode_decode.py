# 10.55
#

class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes the given list of strings and returns encoded string.

        Args:
            strs:list of strings

        Returns:
            encoded string

        Time: O(n) - n = total characters in strs
        Space: O(n)
        """
        encoded = ""

        for word in strs:
            word_len = str(len(word))
            encoded += word_len + "#" + word

        return encoded

    def decode(self, s: str) -> list[str]:
        """Decodes the given encoded string.

        Args:
            s: encoded string

        Returns:
            list of strings

        Time: O(n) - total characters in s
        Space: O(1)
        """
        result = []
        index = 0
        left = 0

        while index < len(s):

            while s[index] != "#":
                index += 1

            word_len = int(s[left : index])
            result.append(s[index + 1 : index + 1 + word_len])
            index = index + 1 + word_len
            left = index

        return result

# 11.03 -> 8 min to solve