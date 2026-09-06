# 8.35


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Find the smallest window of string s that contains every character of string t.

        Args:
            s: String to look within
            t: string to look for

        Returns:
            minimum window of string s that contains every character of string t

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        if len(t) > len(s) or t == "":
            return ""

        # character count string t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # minimum window of string s
        count_s = {}
        have = 0
        need = len(count_t)
        result = [-1, - 1]
        longest = float("inf")
        left = 0

        for index in range(len(s)):

            # add char to count_s
            count_s[s[index]] = count_s.get(s[index], 0) + 1

            # check if that changes have
            if s[index] in count_t and count_s[s[index]] == count_t[s[index]]:
                have += 1

            # check if thats equal to need
            while have == need:

                # current valid window
                curr_window = index - left + 1

                if curr_window < longest:
                    longest = curr_window
                    result = [left, index]

                # reduce the window
                count_s[s[left]] -= 1

                # did that change have
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        start, end = result

        return s[start : end + 1] if longest != float('inf') else ""

s = Solution()
assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert s.minWindow("a", "aa") == ""
assert s.minWindow("a", "a") == "a"
assert s.minWindow("", "ABC") == ""
assert s.minWindow("ABC", "") == ""
assert s.minWindow("XYZ", "ABC") == ""
print('passed')