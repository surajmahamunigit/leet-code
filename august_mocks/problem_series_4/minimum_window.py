# 11.40
# given two strings s, t, asked to find out substring of s that contains whole t


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Find minimum window of string s that contains whole string t.

        Args:
            s: string to look within
            t: string to look for

        Returns:
            substring of s that contains t

        Time: O(n) - n = len(s)
        Space: O(n)
        """
        if t == "":
            return ""


        # character count for t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1


        # character count s
        count_s = {}
        res = [-1,-1]
        longest = float("inf")
        have = 0
        need = len(count_t)
        left = 0

        for index in range(len(s)):

            # add char to count_s
            count_s[s[index]] = count_s.get(s[index], 0) + 1

            if s[index] in count_t and count_s[s[index]] == count_t[s[index]]:
                have += 1

            # check for have == need
            while have == need:

                # check window length
                curr_len = index - left + 1

                if curr_len < longest:
                    res = [left, index]
                    longest = curr_len

                # remove char on left
                count_s[s[left]] -= 1

                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        start, end = res
        return s[start : end + 1] if longest != float("inf") else ""

s = Solution()

assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert s.minWindow("a", "aa") == ""
assert s.minWindow("a", "a") == "a"
assert s.minWindow("", "ABC") == ""
assert s.minWindow("ABC", "") == ""
assert s.minWindow("XYZ", "ABC") == ""
print("passed")

# 11.55 -> 15 min to solve
# add this problem for one more repetition tomorrow