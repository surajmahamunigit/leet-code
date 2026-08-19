# 4.25
# given s, t two strings and asked to find window  in s that contains whole t


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Find minimum window in string s that contains string t.

        Args:
            s: string to look within
            t: string to look for

        Returns:
            substring in s that contains t

        Time: O(n) - n = len(s)
        Space: O(n)
        """
        if t == "":
            return ""

        # character count string t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # count string s characters
        count_s = {}
        have = 0
        need = len(count_t)
        longest = float("inf")
        res = [-1, -1]
        left = 0

        for index in range(len(s)):
            # add char in map
            count_s[s[index]] = count_s.get(s[index], 0) + 1

            if s[index] in count_t and count_t[s[index]] == count_s[s[index]]:
                have += 1

            # may be have == need
            while have == need:
                curr_len = index - left + 1

                if curr_len < longest:
                    longest = curr_len
                    res = [left, index]

                # remove left char
                count_s[s[left]] -= 1

                if s[left] in count_t and count_t[s[left]] > count_s[s[left]]:
                    have -= 1

                left += 1

        start, end = res

        return s[start: end + 1] if longest != float("inf") else ""

s = Solution()
assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert s.minWindow("a", "aa") == ""
assert s.minWindow("a", "a") == "a"
assert s.minWindow("", "ABC") == ""
assert s.minWindow("ABC", "") == ""
assert s.minWindow("XYZ", "ABC") == ""
print("passed")

# 4.50 -> 25 min to solve
# keep it on list for next 3 days if its already not.