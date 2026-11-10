# 7.10

class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        """Find if permutation of string s1 exist in string s2.

        Args:
            s1: strings permutation to look for
            s2: string to search within

        Returns:
            bool: True if permutation of s1 exist in s2, else False

        Time complexity: O(L2) - L2 = len(s2)

        Space complexity: O(1)
        """
        if len(s1) > len(s2):
            return False

        # character count string s1
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for index in range(len(s1)):
            count_s1[ord(s1[index]) - ord("a")] += 1
            count_s2[ord(s2[index]) - ord("a")] += 1

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

def check(values1, values2, expected):
    result = s.check_inclusion(values1, values2)
    assert result == expected

check("a", "ab", True)
check("ab", "a", False)
check("", "a", True)
check("a", "", False)
check("ab", "abcd", True)
check("bc", "xbcd", True)
check("ab", "ladab", True)

print("all tests passed")