# 11.27
# given string s, t and asked to find min substring of s that contains t

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Find the minimum window in string s that contains t.

        Args:
            s: string to search within
            t: string to look for

        Returns:
            minimum window of string s that contains t

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        if t == "":
            return ""

        # character count string t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # character count string s
        count_s = {}
        left = 0
        have = 0
        need = len(count_t)
        longest = float("inf")
        res = [-1, -1]

        for index in range(len(s)):
            char = s[index]
            # add to count map
            count_s[char] = count_s.get(char, 0) + 1

            # check if char was in t
            if char in count_t and count_s[char] == count_t[char]:
                have += 1

            # check if have == need
            while have == need:

                curr_window = index - left + 1

                if curr_window < longest:
                    res = [left, index]
                    longest = curr_window

                # try to reduce the window size
                count_s[s[left]] -= 1

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

# 11.44 -> 17 min to solve