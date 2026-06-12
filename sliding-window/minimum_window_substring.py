"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"

Time: O(n)
Space: O(n)     # n is length of longer string
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        # char count t
        count_t = {}

        for ch in t:
            count_t[ch] = 1 + count_t.get(ch, 0)


        # trace the window characters
        window = {}
        have = 0    # how many characters "have" satisfied char_count condition
        need = len(count_t)     # how many character "need" to satisfy the condition

        res = [-1, -1]      # final result left and right index
        res_length = float("infinity")      # it will always be less than infinity

        left = 0

        for index in range(len(s)):

            ch = s[index]
            # Add ch to window map
            window[ch] = 1 + window.get(ch, 0)

            # if the current character is in count_t and its character count in window and count_t is same
            if ch in count_t and window[ch] == count_t[ch]:
                have += 1

            # if have is equal to need
            while have == need:

                # update our result for window
                window_length = index + 1 - left

                if window_length < res_length:
                    res = [left, index]
                    res_length = window_length

                # remove characters from left to find min window length
                window[s[left]] -= 1
                # if the current/left character was in count_t and its character count in window has become less than count_t for same character
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        left, right = res
        return s[left: right+1] if res_length != float("infinity") else ""


result = Solution().minWindow("OUZODYXAZV", "XYZ")
print(result)

