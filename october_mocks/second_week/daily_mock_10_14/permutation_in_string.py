# 12.42

# given -> two strings
# asked -> to find out if s1's permutation exist in s2

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Find out if any permutation of string s1 exist in string s2.

        Args:
            s1 (str): strings permutation to look for
            s2 (str): string to look within

        Returns:
            bool: True if s1's permutation exist in s2, else False

        Time complexity: O(n) - n = len(s2)

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
            count_s2[ord(s2[left]) - ord("a")] -= 1
            left += 1
            count_s2[ord(s2[index]) - ord("a")] += 1

            if count_s1 == count_s2:
                return True

        return False

# 12.50 -> 8 minutes to solve problem
# git commit -> feat: add permutation in string solution

s = Solution()
assert s.checkInclusion("abc", "cbaebabacd") == True
assert s.checkInclusion("abc", "ccccbbbbaaaa") == False
assert s.checkInclusion("hello", "ooolleoooleh") == False
assert s.checkInclusion("aab", "baa") == True
assert s.checkInclusion("aab", "abbaa") == True
assert s.checkInclusion("z", "abc") == False
assert s.checkInclusion("abcd", "abc") == False
assert s.checkInclusion("a", "b") == False
assert s.checkInclusion("ab", "ab") == True
assert s.checkInclusion("ab", "aa") == False
assert s.checkInclusion("xyz", "aaaxzyaaa") == True
assert s.checkInclusion("abca", "bcaabc") == True
assert s.checkInclusion("a" * 5000, ("a" * 4999 + "b") * 2) == False