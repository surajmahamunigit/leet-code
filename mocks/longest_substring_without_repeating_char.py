# algorithm
# Use set seen = {} to store already seen characters. and left = 0, max_len =0
# for every char at index i in given string,
# check if its present in set seen, start removing characters at s[left] from set until recent char is not removed.
# every time we remove character, move left by 1 and  we measure length of substring as (i - left) then compare with max_len and store max_length.
# if char is not present, then we add it to the set
# in end return max_len


#example
# s="zxyzxyz", left=0, max_len = 0
# index = 0, char = z -> seen = {z}, max_len = 1-0= 1
# index = 1, char = x -> seen = {z,x}, max_len = 2-0= 2
# index = 2, char = y -> seen = {z,x,y}, max_len = 3-0= 3
# index = 3, char = z -> present in seen -> remove s[left]=s[0]=z from the set, left = 1, max_len = 3 -> seen = {x, y, z}
# index = 4, char = x -> present in seen -> remove s[left]=s[1]=x from the set, left = 2, max_len = 3 , seen = { y, z, x}
# index = 5, char = y -> present in seen -> remove s[left]=s[2]=y from the set, left = 3, max_len = 3 , seen = {  z, x,y}
# index = 6, char = z -> present in seen -> remove s[left]=s[3]=z from the set, left = 4, max_len = 3 , seen = {  x,y,z}
# return max_len = 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find the length of longest substring without repeating characters.

        Args:
            s: given string

        Returns:
            length of longest substring without repeating characters

        Time:O(n) - n = len(s)
        Space: O(n)
        """

        max_len = 0
        seen = set()
        left = 0

        for index in range(len(s)):

            char = s[index]
            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            curr_length = index - left + 1
            max_len = max(max_len, curr_length)

        return max_len

s = Solution()
assert s.lengthOfLongestSubstring("zxyzxyz") == 3
assert s.lengthOfLongestSubstring("xxxx") == 1
print("passed")