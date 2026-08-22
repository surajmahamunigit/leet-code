# 2.43
# given list of strings, asked to encode these string and return one encoded string
# accept encoded string as input and return list of encoded words in it.

class Solution:

    def encode(self, strs: list[str]) -> str:
        """Encode the given list of strings and return an encoded string.

        Args:
            strs: list of strings

        Returns:
            encoded string

        Time: O(n) - n = len(strs)
        Space: O(1)
        """

        result = ""

        for word in strs:
            word_len = len(word)
            result += str(word_len) + "#" + word

        return result


    def decode(self, s: str) -> list[str]:
        """Decode the given string and return list of encoded words.

        Args:
            s: encoded string

        Returns:
            list of encoded words

        Time: O(n) - n = total characters in strs
        Space: O(1)
        """

        word_list = []
        left = 0
        index = 0
        while index < len(s):


            while s[index] != "#":
                index += 1

            word_len = int(s[left : index])

            word_list.append(s[index + 1 : index + 1 + word_len])

            index = index + 1 + word_len
            left = index

        return word_list

s = Solution()
assert s.decode(s.encode(["Hello", "World"])) == ["Hello", "World"]
assert s.decode(s.encode(["5#Hi", "a"])) == ["5#Hi", "a"]
assert s.decode(s.encode([])) == []
print("passed")

# 3.02 -> 17 min to solve