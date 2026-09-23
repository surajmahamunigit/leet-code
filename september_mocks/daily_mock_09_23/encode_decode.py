# 11.31

class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encode the given list of strings into encoded string.

        Args:
            strs (list[str]): list of strings

        Returns:
            str: encoded string

        Time: O(n) - n = number of characters in strs

        Space: O(n)
        """
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded


    def decode(self, s: str) -> list[str]:
        """Decode the string into a list of strings.

        Args:
            s (str): encoded string

        Returns:
            list[str]: decode the string and return list of words

        Time: O(n) - n = number of characters in str

        Space: O(n)
        """
        result = []
        index = 0
        while index < len(s):
            left = index
            while s[index] != "#":
                index += 1

            word_len = int(s[left : index])

            result.append(s[index + 1 : index + 1 + word_len])

            index = index + 1 + word_len

        return result

p = Solution()

print(p.decode(p.encode(strs = ["Hello","World"])))
print(p.decode(p.encode(strs = [""])))

