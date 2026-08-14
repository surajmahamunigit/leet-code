# 3.30

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Check if any permutation of s1 exists in s2.

        Args:
            s1: target string
            s2: string to look within

        Returns:
            True if permutation of s1 exist in s2

        Time: O(n) - n = len(s2)
        Space: O(1)
        """

        if len(s1) > len(s2):
            return False

        # character count s1 and s2 till len(s1)
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        for index in range(len(s1)):
            count_s1[ord(s1[index]) - ord("a")] += 1
            count_s2[ord(s2[index]) - ord("a")] += 1

        if count_s1 == count_s2:
            return True

        for index in range(len(s1), len(s2)):
            count_s2[ord(s2[index]) - ord("a")] += 1
            count_s2[ord(s2[index - len(s1)]) - ord("a")] -= 1

            if count_s1 == count_s2:
                return True

        return False

s = Solution()
assert s.checkInclusion("ab", "eidbaooo") == True
assert s.checkInclusion("ab", "eidboaoo") == False
assert s.checkInclusion("adc", "dcda") == True    # last window in s2 matches
assert s.checkInclusion("a", "a") == True
assert s.checkInclusion("abc", "ab") == False
print("passed")

# 3.44 -> 14 min to solve
