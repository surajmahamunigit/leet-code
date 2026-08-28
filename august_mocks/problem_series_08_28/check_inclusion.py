# 2.31

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Find out if any permutation of string s1 is in s2.

        Args:
            s1: string to look for
            s2: string to look within

        Returns:
            True if s1 is in s2, else False

        Time: O(n) - n = len(s2)
        Space: O(1)
        """

        if len(s1) > len(s2):
            return False

        # character count s1
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for index in range(len(s1)):
            count_s1[ord(s1[index]) - ord("a")] += 1
            count_s2[ord(s2[index]) - ord("a")] += 1

        # check if they are equal
        if count_s1 == count_s2:
            return True

        # check in remaining s2
        left = 0
        for index in range(len(s1), len(s2)):

            count_s2[ord(s2[index]) - ord("a")] += 1
            count_s2[ord(s2[left]) - ord("a")] -= 1
            left += 1

            if count_s1 == count_s2:
                return True

        return False

s = Solution()
assert s.checkInclusion("ab", "eidbaooo") == True
assert s.checkInclusion("ab", "eidboaoo") == False
assert s.checkInclusion("adc", "dcda") == True
assert s.checkInclusion("a", "a") == True
assert s.checkInclusion("abc", "ab") == False
print("passed")

# 2.38 -> 7 min to solve