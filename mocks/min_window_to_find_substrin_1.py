class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Find the substring in s that contains whole t string.

        Args:
            s: string to look within
            t: string to look for

        Returns:
            minimum length substring of s that contains t

        Time: O(m+n) - m = len(t), n = len(s)
        Space: O(m+n)
        """

        if t == "":
            return ""

        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1


        count_s = {}
        left = 0
        have = 0
        need = len(count_t)
        result = [-1, -1]
        result_len = float("infinity")

        for index in range(len(s)):
            char = s[index]

            # add to count_s
            count_s[char] = count_s.get(char, 0) + 1

            # added char might be in t
            if char in count_t and count_s[char] == count_t[char]:
                have += 1

            # check have == need
            while have == need:

                # check result
                if (index - left + 1) < result_len:
                    result = [left, index]
                    result_len = index - left + 1

                # remove leftmost char to reduce length of window
                count_s[s[left]] -= 1
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        left, right = result

        return s[left : right + 1] if result_len != float("infinity") else ""


s = Solution()
assert s.minWindow("xyaz", "xyz") == "xyaz"
assert s.minWindow("OUZODYXAZV", "XYZ") == "YXAZ"
assert s.minWindow("xyaz", "") == ""
print("passed")
