# 2.14

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Find the shortest substring of s that contains t.

        Args:
            s: string to search within
            t: target string

        Returns:
            substring of s that contains t

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
        have = 0
        need = len(count_t)     # only unique
        longest = float("inf")
        res = [-1, -1]
        left = 0

        for index in range(len(s)):
            char = s[index]

            # add char to count_s
            count_s[char] = count_s.get(char, 0) + 1

            if char in count_t and count_t[char] == count_s[char]:
                have += 1

            while have == need:
                curr_window = index - left + 1
                if curr_window < longest:
                    res = [left, index]
                    longest = curr_window

                count_s[s[left]] -= 1
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        start, end = res
        return s[start : end+1]

s = Solution()
assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert s.minWindow("a", "aa") == ""
assert s.minWindow("a", "a") == "a"
assert s.minWindow("", "ABC") == ""
assert s.minWindow("ABC", "") == ""
assert s.minWindow("XYZ", "ABC") == ""
print("passed")

# 2.31 -> 17 min to solve