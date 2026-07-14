class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Args:
            s: input string
            t : target string

        Returns:
            smallest substring of s that contains t if found, otherwise ""

        Time: O(n) - n  len(s)
        Space: O(n) - n because string s and t can contain uppercase, lowercase, digits, special characters
        """

        # step 1 : check if t is empty or not
        if t == "":
            return ""


        # step 2: otherise, count string t characters
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1


        # step 3: now trace string s
        window_s = {}       # string s character count
        left = 0
        have = 0
        need = len(count_t)     # check unique character

        result = [-1, -1]                   # assume
        result_len = float("infinity")      # assume

        for index in range(len(s)):

            # 1. Add character to the window
            char = s[index]
            window_s[char] = window_s.get(char, 0) + 1

            # Check if same char was in string t and both have same freq
            if char in count_t and window_s[char] == count_t[char]:
                have += 1

            # assume have = need
            while have == need:

                # 1. modify result and result length, only if is smaller than old
                if (index - left + 1) < result_len:
                    result = [left, index]
                    result_len = (index - left + 1)

                # 2. now drop left-most char, and check if thats smallest substring
                left_char = s[left]
                window_s[left_char] -= 1

                # check if dropped char was in t and now char freq in window_s < count_t
                if left_char in count_t and window_s[left_char] < count_t[left_char]:
                    have -= 1

                # move left index
                left += 1

        start, end = result

        return s[start: end + 1] if result_len != float("infinity") else ""

result = Solution().minWindow(s="AABCAD", t="ABD")
print(result)