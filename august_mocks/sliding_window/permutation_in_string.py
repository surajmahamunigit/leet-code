# 1.02

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Find if any combination string s1 exist in string s2.

        Args:
            s1: target string
            s2: string to look within

        Returns:
            True if any combination of s1 exist in s2, else False

        Time: O(n) - n = len(s2)
        Space: O(1)
        """

        if len(s1) > len(s2):
            return False

        # character count of string s1
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        for index in range(len(s1)):
            count_s1[ord(s1[index]) - ord("a")] += 1
            count_s2[ord(s2[index]) - ord("a")] += 1

        if count_s1 == count_s2:
            return True


        # trace string s2

        for right in range(len(s1), len(s2)):

            count_s2[ord(s2[right]) - ord("a")] += 1
            count_s2[ord(s2[right - len(s1)]) - ord("a")] -= 1

            if count_s1 == count_s2:
                return True



        return False

s = Solution()
assert s.checkInclusion("ab", "eidbaooo") == True     # "ba" is a permutation of "ab"
assert s.checkInclusion("ab", "eidboaoo") == False
assert s.checkInclusion("adc", "dcda") == True         # last window in s2 matches
assert s.checkInclusion("a", "a") == True               # single char, exact match
assert s.checkInclusion("abc", "ab") == False            # s1 longer than s2
print("passed")