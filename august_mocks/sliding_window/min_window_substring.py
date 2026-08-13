# 11.24

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Find minimum window in string s that contains t.

        Args:
            s: string to look within
            t: target string

        Returns:
            minimum window in string s containing t

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        if t == "":
            return ""

        # count char count in t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # count string s characters
        left = 0
        count_s = {}
        have = 0
        need = len(count_t)             # unique chars in t
        res = [-1,-1]
        longest = float("inf")

        for index, char in enumerate(s):

            # add char in count_s
            count_s[char] = count_s.get(char, 0) + 1

            # check if that char is also present in count_t
            if char in count_t and count_s[char] == count_t[char]:
                have += 1

            # if by chance have == need
            while have == need:

                curr_len = index - left + 1
                if curr_len < longest:
                    longest = curr_len
                    res = [left, index]

                # remove s[left] to reduce length and check again
                count_s[s[left]] -= 1

                # if by chance we remove char we needed
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        start, end = res
        return s[start : end + 1]

s = Solution()
assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert s.minWindow("a", "aa") == ""
assert s.minWindow("a", "a") == "a"
assert s.minWindow("", "ABC") == ""
assert s.minWindow("ABC", "") == ""
assert s.minWindow("XYZ", "ABC") == ""
print("passed")

# 11.45 -> 21 minutes