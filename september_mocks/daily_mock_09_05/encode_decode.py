# 6.27

class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encode the given list of strings.

        Args:
            strs: list of strings

        Returns:
            str: encoded string containing all words from strs list

        Time: O(n) - n = len(encoded)
        Space: O(n)
        """
        encoded = ""

        for word in strs:
            word_len = str(len(word))
            encoded += word_len + "#" + word

        return encoded

    def decode(self, s: str) -> list[str]:
        """Decode the given string and return all strings as list.

        Args:
            s (str): given encoded string

        Returns:
             list[str]: list of word decoded from given string

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        decoded = []
        index = 0
        while index < len(s):
            left = index
            while s[index] != "#":
                index += 1

            word_len = int(s[left : index])
            decoded.append(s[index + 1 : index + 1 + word_len])

            index = index + 1 + word_len

        return decoded

s = Solution()
assert s.decode(s.encode(["Hello", "World"])) == ["Hello", "World"]
assert s.decode(s.encode(["5#Hi", "a"])) == ["5#Hi", "a"]
assert s.decode(s.encode([])) == []
print('passed')