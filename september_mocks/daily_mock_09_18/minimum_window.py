# 12.06

class Solution:
    def min_window(self, s: str, t: str) -> str:
        """find the minimum window of string s that contains string t.

        Args:
            s (str): string to look withing
            t (str): string to look for

        Returns:
            int: minimum window of string s that contains string t

        Time: O(n) - n = len(s)

        Space: O(n)
        """

        # Input: s = "OUZODYXAZV", t = "XYZ"

        # base condition
        if len(t) > len(s):
            return ""

        # character count string t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # search string s
        longest = float('inf')
        result = [-1, -1]
        have = 0
        need = len(count_t)
        left = 0
        count_s = {}
        for index in range(len(s)):

            count_s[s[index]] = count_s.get(s[index], 0) + 1

            # check if have increase
            if s[index] in count_t and count_t[s[index]] == count_s[s[index]]:
                have += 1

            # check if have == need
            while have == need:
                curr_len = index - left + 1

                if curr_len < longest:
                    longest = curr_len
                    result = [left, index]

                # take left char out and check again
                count_s[s[left]] -= 1

                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        start, end = result
        return s[start : end+1] if longest != float('inf') else ""

s = Solution()
print(s.min_window(s = "OUZODYXAZV", t = "XYZ"))
print(s.min_window(s = "xyz", t = "xyz"))
print(s.min_window(s = "x", t = "xy"))