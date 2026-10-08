# 12.07

class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encode the given list of string into a string.

        Args:
            strs (list[str]): list of string

        Returns:
            str: encoded string

        Time complexity: O(n) - n = total number of characters in given strs

        Space complexity: O(n)
        """

        result = ""

        for word in strs:
            word_len = str(len(word))
            result +=  word_len + "#" + word

        return result

    def decode(self, s: str) -> list[str]:
        """Decode the given string.

        Args:
            s (str): given encoded string

        Returns:
            list[str]: list of words by decoding given string

        Time complexity: O(n) - n = total number of characters in given string

        Space complexity: O(n)
        """
        result = []

        index = 0
        while index in range(len(s)):
            left = index
            while s[index] != "#":
                index += 1

            word_len = int(s[left : index])

            result.append(s[index + 1 : index + 1 + word_len])
            index = index + 1 + word_len

        return result

# 12.39 -> 32 minutes to solve problem
# git commit -> feat: add encode and decode solution

s = Solution()
cases = [
    ["neet", "code", "love", "you"],
    ["we", "say", ":", "yes"],
    [],
    [""],
    ["", ""],
    ["4#abc", "#", "3#", "12#"],
    ["a,b", "c|d", "e#f", "g:h", "1#"],
    ["héllo", "日本語", "🙂"],
    ["a" * 1000, "b\nc", " ", "\t"],
    ["#", "##", "###"],
    ["10#aaaaaaaaaa", "0#", "#0"],
]
for c in cases:
    assert s.decode(s.encode(c)) == c
assert s.encode([]) != s.encode([""])
assert s.decode(s.encode(["x"] * 5000)) == ["x"] * 5000

