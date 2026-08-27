# 12.50
# given s1 and s2. and asked to find out if any permutation of s1 exist as substring in s2

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Find out if any permutation of s1 exist as substring s2.

        Args:
            s1: target string
            s2: string to search within

        Returns:
            True if permutation of s1 exist as substring in s2, else False

        Time: O(n) - n = len(s2)
        Space: O(1)
        """

        if len(s1) > len(s2):
            return False

        # # character count s1
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for index in range(len(s1)):
            count_s1[ord(s1[index]) - ord("a")] += 1
            count_s2[ord(s2[index]) - ord("a")] += 1

        # check if thats the target substring
        if count_s1 == count_s2:
            return True

        # check on remaining s2
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

# 12.59 -> 9 min to solve