# 6.05

class Solution:
    def encode(self, strs: list[str]) -> str:
        """encode the given list of strings and return a string.

        Args:
            strs: list of strings

        Returns:
            encoded string

        Time: O(n) - n = total characters in lists
        Space: O(n)
        """
        res = ''
        for word in strs:
            res += str(len(word)) + "#" + word

        return res


    def decode(self, s: str) -> list[str]:
        """Decode the given string and return original words.

        Args:
            s: encoded string

        Returns:
            decodes the string and returns original words as a list

        Time: O(n) - n = total characters in lists
        Space: O(n))
        """
        res = []

        index = 0
        while index in range(len(s)):
            left = index
            while s[index] != "#":
                index += 1

            word_len = int(s[left : index])
            word = s[index + 1 : index + 1 + word_len]
            res.append(word)
            index = index + 1 + word_len

        return res

s = Solution()
assert s.decode(s.encode(["Hello", "World"])) == ["Hello", "World"]
assert s.decode(s.encode(["5#Hi", "a"])) == ["5#Hi", "a"]
assert s.decode(s.encode([])) == []
print("passed")

# 6.19 -> 14 min to solve