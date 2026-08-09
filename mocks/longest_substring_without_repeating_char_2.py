# algorithm
# given string and we have to find out longest substring without repeating any character
# we will use set to store already seen char.
# left = 0, for every index in range(len(s))
# if s[index] in seen -> remove s[index] from set and move left += 1 to keep window size same
# if its not there, add it to the set and check curr_len = index - left + 1, compare with max_len and save it
# return max_len

class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        """Find the length of longest substring in s without repeating characters.

        Args:
            s: input string

        Returns:
            length of longest substring of s without repeating characters

        Time: O(n) - n = length of longest string
        Space: O(n)
        """
        max_len = 0
        left = 0
        right = 0
        seen = set()

        while right < len(s):

            # if its already present in set
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # if not there, then add it to set and count length
            seen.add(s[right])
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
            right += 1

        return max_len

s = Solution()
#res = s.length_of_longest_substring("zxyzxyz")
res = s.length_of_longest_substring(s = "xxxx")
print(res)
