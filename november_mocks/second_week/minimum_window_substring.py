# 8.36

class Solution:
    def minimum_window(self, s: str, t: str) -> int:
        """Find shortest substring of s that contains t.

        Args:
            s: string to look within
            t: string to look for

        Returns:
            str: shortest substring of s that contains t, else returns ""

        Time complexity: O(n) - n = len(s)

        Space complexity: O(n)
        """

        if len(t) == 0:
            return ""

        # character count string t
        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        # check String s
        left = 0
        count_s = {}
        have = 0
        need = len(count_t)
        min_window = float("inf")
        result = [-1, -1]

        for index in range(len(s)):
            count_s[s[index]] = count_s.get(s[index], 0) + 1

            if s[index] in count_t and count_t[s[index]] == count_s[s[index]]:
                have += 1

            while have == need:
                curr_window = index - left + 1

                if curr_window < min_window:
                    min_window = curr_window
                    result = [left, index]

                count_s[s[left]] -= 1

                if s[left] in count_t and count_t[s[left]] > count_s[s[left]]:
                    have -= 1

                left += 1


        start, end = result

        return s[start : end + 1] if min_window != float("inf") else ""


p = Solution()

def check(values1, values2, expected):
    result = p.minimum_window(values1, values2)
    assert result == expected

check("abcd", "", "")
check("xyz", "ab", "")
check("abcd", "a", "a")
check("abcd", "ab", "ab")
check("abcd", "abc", "abc")
check("abcd", "cd", "cd")
check("abcd", "bgf", "")
check("abcd", "ac", "abc")
print("all tests passed")