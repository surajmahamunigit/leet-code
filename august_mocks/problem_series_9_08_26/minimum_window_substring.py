# 1.04

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Find minimum window substring in s that contains t.

        Args:
            s: string to search within
            t: target string

        Returns:
            minimum window substring of s

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        # character count t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # character count s
        count_s = {}
        res = [-1, -1]
        longest = float("inf")
        have = 0
        need = len(count_t)
        left = 0

        for index in range(len(s)):

            # add char to count
            count_s[s[index]] = count_s.get(s[index], 0) + 1

            # check have has increase or not
            if s[index] in count_t and count_s[s[index]] == count_t[s[index]]:
                have += 1

            # check if have == need
            while have == need:

                # count length
                curr_len = index - left + 1

                # check if its shortest
                if curr_len < longest:
                    res = [left, index]
                    longest = curr_len

                count_s[s[left]] -= 1

                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        start, end = res

        return s[start : end+1] if longest != float('inf') else ""

s = Solution()
res = s.minWindow("XZ","XYZ")
print(res)

# 1.22 -> 18 min