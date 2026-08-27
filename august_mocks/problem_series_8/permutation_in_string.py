# 1.21

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Find if s2 contains any permutation of s1.

        Args:
            s1: string to look for
            s2: string to look within

        Return:
            True if s2 contains s1, else False

        Time: O(n) - n = len(s2)
        Space: O(1)
        """

        # character count s1
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for index in range(len(s1)):
            count_s1[ord(s1[index]) - ord("a")] += 1
            count_s2[ord(s2[index]) - ord("a")] += 1

        if count_s1 == count_s2:
            return True

        left = 0
        for index in range(len(s1), len(s2)):
            char = s2[index]

            count_s2[ord(char) - ord("a")] += 1
            count_s2[ord(s2[left]) - ord("a")] -= 1
            left += 1

            if count_s2 == count_s1:
                return True

        return False

s = Solution()
res = s.checkInclusion(s1 = "abc", s2 = "lecaabee")
print(res)

# 1.29 -> 8 min to solve