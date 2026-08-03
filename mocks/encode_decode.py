# algorithm
# strs = ["Hello","World"]

# encode() function:
# for each word in string array -> result += convert to string len(word) + "#" " word
# and result will return one string represented like 5#Hellow5#World

# decode() function:
#  decode function will accept encode functions output as input -> s = 5#Hellow5#World
# assume  pointers left =0
# while left < len(s):
# right = left,
# check while s[right] != "#": right += 1, when while loop breaks, find first word length by converting to int s[left:right], use it to get the word from string
# new_word = s[right+1 : right+1+word_length], add it to result array
# move left = right + 1 + word length, that will skipp till end of first word, so even if word contains any special characters, we skip over them.
# in end left will len(s) and it will break the loop and we return result array


# example:
# encode():
# strs = ["Hello","World"],s= ""
# word_length = 5, s = 5#Hellow
# word_length = 5, s = 5#Hellow5#World

# decode:
# s = 5#Hellow5#World
# left = 0, right = 1,word_len = s[0:1] = 5, new_word = s[1+1 : 1+1+5]= ["Hello"], left = 1+1+5
# left = 7, right = 9, word_len = s[7:9]= 5, new_word = s[9+1 : 9+1+5] = ["Hello", "World"]


class Solution:

    def encode(self, strs: list[str]) -> str:
        """Return encoded string using all words in the given string array.

        Args:
            strs: given string array

        Returns:
            single encoded string

        Time: O(n) - n = len(strs)
        Space: O(n) - for result string
        """

        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word               # typecast to str

        return result

    def decode(self, s: str) -> list[str]:
        """Return array containing all the words in the given string.

        Args:
            s: encoded string containing all words from given array

        Returns:
            decoded list of words from given string

        Time: O(n) - n = len(s)
        Space: O(1) - for result
        """
        result = []
        left = 0

        while left < len(s):
            right = left

            while s[right] != "#":
                right += 1

            word_len = int(s[left : right])                     # typecast to int
            new_word = s[right+1 : right + 1 + word_len]
            result.append(new_word)
            left = right + 1 + word_len

        return result

s = Solution()
assert s.decode(s.encode(["Hello", "World"])) == ["Hello", "World"]
assert s.decode(s.encode(["5#Hi", "a"])) == ["5#Hi", "a"]
assert s.decode(s.encode([])) == []
print("passed")