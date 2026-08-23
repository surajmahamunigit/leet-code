# 12.43
# given two strings s, t and asked to find minimum window in s that contains t

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Find minimum window in string s that contains string t.

        Args:
            s: string to look within
            t: target string

        Returns:
            minimum window substring in s that contains t

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        if t == "":
            return ""

        # character count t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # character count s
        count_s = {}
        res = [-1, - 1]
        longest = float("inf")
        left = 0
        have = 0
        need = len(count_t)

        for index in range(len(s)):
            # add char
            char = s[index]
            count_s[char] = count_s.get(char, 0) + 1

            # check have increased or not
            if char in count_t and count_s[char] == count_t[char]:
                have += 1

            # check if have == need
            while have == need:

                # possible window length
                curr_len = (index - left + 1)
                if curr_len < longest:
                    res = [left, index]
                    longest = curr_len

                # reduce window size
                count_s[s[left]] -= 1

                # check have reduced or not
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        start, end = res

        return s[start : end+1] if longest != float("inf") else ""

s = Solution()
assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert s.minWindow("a", "aa") == ""
assert s.minWindow("a", "a") == "a"
assert s.minWindow("", "ABC") == ""
assert s.minWindow("ABC", "") == ""
assert s.minWindow("XYZ", "ABC") == ""
print("passed")

# 12.56 -> 13 minutes to solve