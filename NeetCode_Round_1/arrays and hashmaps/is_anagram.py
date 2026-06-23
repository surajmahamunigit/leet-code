class Solution:
    def is_anagram(self, word1: str, word2: str) -> bool:
        """
        Args:
            word1: first string
            word2: second string

        Returns:
            boolean: True if Anagram, False otherwise

        Time: O(n)  # For each character in the string
        Space: O(n) # for character count
        """

        # Both strings need to be same length
        if len(word1) != len(word2):
            return False

        # Character counts of both strings must be same
        word1_count = {}
        word2_count = {}

        for i in range(len(word1)):

            word1_count[word1[i]] = 1 + word1_count.get(word1[i], 0)
            word2_count[word2[i]] = 1 + word2_count.get(word2[i], 0)

        return word1_count == word2_count

result = Solution().is_anagram(word1="racecar", word2="car")
print(result)