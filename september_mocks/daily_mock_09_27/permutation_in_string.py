# 8.05

class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        """Check if any permutation of string s1 exist in s2.

        Args:
            s1, s2 (string): given lowercase strings

        Returns:
            bool: True if any permutation of s1 exist in s2

        Time: O(n) - n = len(s2)

        Space: O(1)
        """

        # s1 = "abc", s2 = "lecabee"
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

        # character count remaining s2
        left = 0
        for index in range(len(s1), len(s2)):
            count_s2[ord(s2[index]) - ord("a")] += 1
            count_s2[ord(s2[left]) - ord("a")] -= 1
            left += 1

            if count_s1 == count_s2:
                return True

        return False

s = Solution()
print(s.check_inclusion("ab", "abc"))
print(s.check_inclusion(s1 = "abc", s2 = "lecabee"))
print(s.check_inclusion(s1 = "abc", s2 = "a"))