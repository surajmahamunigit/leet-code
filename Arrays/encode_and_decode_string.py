"""
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]
"""

class Solution:

    def encode(self, strs: list[str]) -> str:

        result=''

        for string in strs:
            result = result+str(len(string))+'#'+string

        return result

    def decode(self, s: str) -> list[str]:
        result = []
        i=0

        while i<len(s):
            j=i

            # Find the length of first string in long string
            while s[j] != '#':
                j+=1

            str1_len= int(s[i:j])
            result.append(s[j+1:j+str1_len+1])

            # new word starting index
            i=j+str1_len+1

        return result


# Encode the list of strings
s=Solution()
en_result= s.encode(['raj','kiran','diva'])
print(f'Printing encoded strs: {en_result}')


# Decode the string
de_result= s.decode(en_result)
print(f'Printing decoded string list:{de_result}')