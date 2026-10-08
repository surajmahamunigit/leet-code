# 10.12

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Find out if the permutation of string s1 exist in string s2.

        Args:
            s1 (str): strings permutation to look for
            s2 (str): string to look within

        Returns:
            bool: True if permutation of s1 exist in s2, False otherwise

        Time complexity: O(n) - n = len(s2)

        Space complexity: O(1)
        """
        if len(s1) > len(s2):
            return False

        # character count s1
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        for index in range(len(s1)):
            count_s1[ord(s1[index]) - ord("a")] += 1
            count_s2[ord(s2[index]) - ord("a")] += 1

        if count_s1 == count_s2:
            return True

        # check in the remaining s2
        left = 0
        for index in range(len(s1), len(s2)):
            count_s2[ord(s2[index]) - ord("a")] += 1
            count_s2[ord(s2[left]) - ord("a")] -= 1
            left += 1

            if count_s1 == count_s2:
                return True

        return False

# 10.21 -> 9 minutes to solve the problem
# git commit -> feat: add permutation in string solution

s = Solution()
assert s.checkInclusion("ab", "eidbaooo") == True
assert s.checkInclusion("ab", "eidboaoo") == False
assert s.checkInclusion("adc", "dcda") == True
assert s.checkInclusion("a", "a") == True
assert s.checkInclusion("abc", "ab") == False
assert s.checkInclusion("abc", "ccccbbbbaaaa") == False
assert s.checkInclusion("", "abc") == True
assert s.checkInclusion("", "") == True