# 9.59
# given list of string and asked to encode it and then decode it and return encoded strings as list.

class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encode the given list of strings and return a string.

        Args:
            strs: list of strings

        Returns:
            encoded string

        Time: O(n) - n = total characters in strs
        Space: O(1)
        """
        encoded = ""

        for word in strs:
            word_len = len(word)
            encoded += str(word_len) + "#" + word

        return encoded

    def decode(self, s: str) -> list[str]:
        """Decode the given string and return list of decoded words.

        Args:
            s: given encoded string

        Returns:
            decoded list of words

        Time: O(n) - n = total characters in strs
        Space: O(1)
        """
        result = []

        while index < len(s):
            left = index
            while s[index] != "#":
                continue

            word_len = int(s[left : index])
            result.append(s[index + 1 : index + 1 + word_len])
            index = index + 1 + word_len

        return result


# 10.09 -> 10 min to solve