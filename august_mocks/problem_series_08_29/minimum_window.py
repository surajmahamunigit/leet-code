# 8.08


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Return shortest substring of s that contains every character of t.

        Args:
            s: string to look within
            t: target string

        Returns:
            minimum window in string s that contains every character of t

        Time: O(n) - n = len(s)
        Space: O(n)
        """
        if t == "":
            return ""

        # character count the string t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # character count string s
        count_s = {}
        have = 0
        need = len(count_t)
        left = 0
        longest = float('inf')
        result = [-1, -1]
        for index in range(len(s)):
            char = s[index]

            count_s[char] = count_s.get(char, 0) + 1

            # check if have increase
            if char in count_t and count_s[char] == count_t[char]:
                have += 1

            # check have == need
            while have == need:

                # check current window length
                curr_len = index - left + 1

                if curr_len < longest:
                    longest = curr_len
                    result = [left, index]

                # reduce window
                count_s[s[left]] -= 1

                # check if have decreased
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        start, end = result

        return s[start : end + 1] if longest != float("inf") else ''

s = Solution()
assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert s.minWindow("a", "aa") == ""
assert s.minWindow("a", "a") == "a"
assert s.minWindow("", "ABC") == ""
assert s.minWindow("ABC", "") == ""
assert s.minWindow("XYZ", "ABC") == ""
print('passed')

# 8.25 -> 17 min to solve