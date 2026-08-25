# 8.21
# given s1, s2 and asked if any permutation of s1 is in s2
# characetr count s1
# character count s2


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Check if any permutation of s1 is in s2.

        Args:
            s1: string to look for
            s2: string to search within

        Returns:
            True if any permutation o s1 is in s2, else False

        Time: O(n) - n = len(s2)
        Space: O(1)
        """
        if len(s2) < len(s1):
            return False

        # character count s1
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for index in range(len(s1)):
            count_s1[ord(s1[index]) - ord("a")] += 1
            count_s2[ord(s2[index]) - ord("a")] += 1

        if count_s1 == count_s2:
            return True

        # check remaining s2
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
res = s.checkInclusion("ab", "eidbaooo")
print(res)

# 8.37 -> 16 min to solve