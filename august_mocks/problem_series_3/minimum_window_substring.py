# 10.49
# given two strings s and t. find minimum window of s that contains whole t string


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Return substring of s that contains whole t string.

        Args:
            s: string to look within
            t: string to look for

        Returns:
            substring of s string that contains t string

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        if t == "":
            return ""

        # character count t string
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # character count string s
        count_s = {}
        res = [-1, -1]
        longest = float('inf')
        have = 0
        need = len(count_t)
        left = 0

        for index in range(len(s)):

            # add new character
            count_s[s[index]] = count_s.get(s[index], 0) + 1

            # check for have increased
            if s[index] in count_t and count_s[s[index]] == count_t[s[index]]:
                have += 1

            # check if have == need
            while have == need:

                # check window length
                curr_len = index - left + 1
                if curr_len < longest:
                    res = [left, index]
                    longest = curr_len

                # remove left character to minimize window size
                count_s[s[left]] -= 1

                # check if have reduced
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        start, end = res

        return s[start : end+1] if longest != float('inf') else ''

s = Solution()
assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert s.minWindow("a", "aa") == ""
assert s.minWindow("a", "a") == "a"
assert s.minWindow("", "ABC") == ""
assert s.minWindow("ABC", "") == ""
assert s.minWindow("XYZ", "ABC") == ""
print("passed")

# 11.03 -> 14 min to solve