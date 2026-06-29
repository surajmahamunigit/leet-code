class Solution:
    def substring(self, s: str) -> int:
        """
        Args:
            S: input string

        Returns:
              length of longest substring without repeating characters

        Time: O(n) - for loop
        Space: O(n) - for char_set
        """

        max_length = 0

        # To store characters and for O(1) lookup
        char_set = set()
        left = 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add new char to char_set and find new max_length
            char_set.add(s[right])
            max_length = max(max_length, (right - left + 1))

        return max_length

result = Solution().substring("zxyzxyzz")
print(result)