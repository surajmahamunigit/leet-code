# 11.28

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Find if any permutation of s2 string exist in s1 string.

        Args:
            s2 (str): string to look within
            s1 (str): strings permutation to look for

        Returns: bool: true if any permutation of s2 exist in s1 else False

        Time: O(n) - n = len(s2)

        Space: O(1)
        """

        # character count s1
        count_s2 = [0] * 26
        count_s1 = [0] * 26

        for index in range(len(s1)):
            count_s1[ord(s1[index]) - ord("a")] += 1
            count_s2[ord(s2[index]) - ord("a")] += 1

        # check possibility
        if count_s1 == count_s2:
            return True

        # check possibility in remaining s2
        left = 0
        for index in range(len(s1), len(s2)):
            count_s2[ord(s2[index]) - ord("a")] += 1
            count_s2[ord(s2[left]) - ord("a")] -= 1
            left += 1

            if count_s1 == count_s2:
                return True

        return False

s = Solution()
print(s.checkInclusion(s1 = "abc", s2 = "lecabee"))
print(s.checkInclusion(s1 = "abc", s2 = "lecaabee"))