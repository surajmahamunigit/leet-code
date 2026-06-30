class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Args:
            s1: pattern string
            s2: string to search within

        Returns:
            True if s2 contains contiguous substring that's permutation of s1

        Time: O(n) - n = len(s2), single pass with O(1) work per slide
        Space: O(1) - fixed array sizes
        """

        n1= len(s1)
        n2= len(s2)

        if n1 > n2:
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(n1):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        # Check window before sliding
        if s1_count == s2_count:
            return True

        # Slide window
        for i in range(n1, n2):
            s2_count[ord(s2[i]) - ord("a")] += 1
            s2_count[ord(s2[i - n1]) - ord("a")] -= 1

            # Check after slide
            if s1_count == s2_count:
                return True

        return False

result = Solution().checkInclusion("ac", "abc")
print(result)