# 8.33

class Solution:
    def min_window(self, s: str, t: str) -> str:
        """Find minimum window of string s that contains string t.

        Args:
            s, t (string): given strings

        Returns:
            str: minimum window of string s that contains t

        Time: O(m+n) - m ,n = lengths of string t and s

        Space: O(m+n)
        """

        # s = "OUZODYXAZV", t = "XYZ"

        if len(t) == 0:
            return ""

        # character count t
        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0 ) + 1

        # check string s
        left = 0
        count_s = {}
        have = 0
        need = len(count_t)
        min_window = float("inf")
        result = [-1, -1]

        for index in range(len(s)):
            ch = s[index]
            count_s[ch] = count_s.get(ch, 0) + 1

            # check if have increased
            if ch in count_t and count_t[ch] == count_s[ch]:
                have += 1

            # if have == need
            while have == need:
                curr_window = index - left + 1

                if curr_window < min_window:
                    min_window = curr_window
                    result = [left, index]

                # remove left char to check for minimum window again
                count_s[s[left]] -= 1

                if s[left] in count_t and count_t[s[left]] > count_s[s[left]]:
                    have -= 1

                left += 1
        start, end = result
        return s[start : end + 1] if min_window != float('inf') else ""

s = Solution()
print(s.min_window(s = "OUZODYXAZV", t = "XYZ"))
print(s.min_window(s = "xyz", t = "xyz"))
print(s.min_window(s = "x", t = "xy"))