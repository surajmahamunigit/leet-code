# 10.21
# given list of strings and asked to encode the strings and return one string
# then take that string as input to decode and asked to decode string and return list of decoded words from string

class Solution:

    def encode(self, strs: list[str]) -> str:
        """Encode given list of strings.

        Args:
            strs: list of strings

        Returns:
            encoded string

        Time: O(n) - n = total words in strs
        Space: O(n)
        """
        encoded = ""
        for word in strs:
            word_len = str(len(word))
            encoded += word_len + "#" + word

        return encoded

    def decode(self, s: str) -> list[str]:
        """Decode the given string and return words as list.

        Args:
            s: encoded string

        Returns:
            list of decoded words

        Time: O(n) - n = total characters in strs
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

s = Solution()
assert s.decode(s.encode(["Hello", "World"])) == ["Hello", "World"]
assert s.decode(s.encode(["5#Hi", "a"])) == ["5#Hi", "a"]
assert s.decode(s.encode([])) == []
print('passed')

# 10.31 -> 10 min to solve