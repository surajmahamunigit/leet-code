class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Find minimum length of substring that contains string t.

        Args:
            s: string to search within
            t: string to look for

        Returns:
            minimum length of substring of s that contains t

        Time: O(n) - n = len(s)
        Space: O(n)
        """

        if t == "":
            return ""

        if len(s) < len(t):
            return ""


        # count characters on t
        count_t = {}

        for i in range(len(t)):
            count_t[t[i]] = 1 + count_t.get(t[i], 0)


        # start adding string s characters
        left = 0
        count_s = {}
        have = 0
        need = len(count_t)
        res = [-1,-1]
        res_len = float("infinity")

        # ADOBECODEBANC
        for i in range(len(s)):

            # add char
            char = s[i]
            count_s[char] = 1 + count_s.get(char, 0)

            # check if exist in t
            if char in count_t and count_t[char] == count_s[char]:
                have += 1

            while have == need:

                # calculate result length
                curr_len = i - left + 1
                if curr_len < res_len:
                    res_len = curr_len
                    res = [left , i+1]

                # remove left char
                count_s[s[left]] -= 1

                # check if it exist in t
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                # move left forward
                left += 1

        left, right = res

        return s[left:right] if res_len != float("infinity") else ""


s = Solution()
print(s.minWindow(s="ADOBECODEBANC", t="ABC"))








