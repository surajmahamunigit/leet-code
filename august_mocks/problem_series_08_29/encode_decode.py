# 2.48


class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encode the given list of strings into a single string.

        Args:
            strs: list of strings

        Returns:
            encoded string

        Time: O(n) - n = total characters in string s
        Space: O(n)
        """

        encoded = ""
        for word in strs:
            word_len = str(len(word))
            encoded += word_len + "#" + word

        return encoded

    def decode(self, s: str) -> list[str]:
        """Decode the given string and returns all words as list.

        Args:
            s: encoded string

        Returns:
            list of decoded word from encoded string s

        Time: O(n) - n = total characters in string s
        Space: O(n)
        """
        res = []

        index = 0
        while index < len(s):
            left = index

            while s[index] != "#":
                index += 1

            word_len = int(s[left : index])
            res.append(s[index + 1 : index + 1 + word_len])
            index = index + 1 + word_len

        return res

s = Solution()
assert s.decode(s.encode(["Hello", "World"])) == ["Hello", "World"]
assert s.decode(s.encode(["5#Hi", "a"])) == ["5#Hi", "a"]
assert s.decode(s.encode([])) == []
print("passed")

# 3 -> 12 min to solve