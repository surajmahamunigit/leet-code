# 2.31

class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encode the given list of strings and return a string.

        Args:
            strs (list[str]): list of strings

        Returns:
             str: encoded string

        Time complexity: O(E) - E = total encoded string length

        Space complexity: O(E)
        """

        encoded = []
        for word in strs:
            word_len = len(word)
            encoded.append(str(word_len) + "#" + word)

        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        """Decode the given string and return a list of words.

        Args:
            s (str): given encoded string

        Returns:
            list[str]: list of decoded words

        Time complexity: O(E) - c = total number of characters in given list of strings

        Space complexity: O(1)
        """

        decoded = []
        index = 0
        while index < len(s):
            left = index
            while s[left] != "#":
                left += 1

            word_len = int(s[index:left])
            word = s[left + 1: left + 1 + word_len]
            decoded.append(word)

            index = left + 1 + word_len

        return decoded

s = Solution()

def check(values, expected):
    result = s.decode(s.encode(values))
    assert result == expected

check(["Hello", "World"], ["Hello", "World"])
check([""], [""])
print("all tests passed")

# 2.43 -> 12 minutes to solve
# git commit -> feat: add encode decode solution