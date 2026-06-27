class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Args:
            s: string

        Returns:
            bool: True if string is palindrome else False

        Time: O(n) - for all char in string
        Space: O(1) - no extra space
        """

        left = 0
        right = len(s) - 1

        while left < right:

            # Check char at left and right index is alpha-numeric or not
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1

            # Compare
            if s[left].lower() != s[right].lower():
                return False

            # modify indexes
            left += 1
            right -= 1

        return True

result = Solution().validPalindrome("race car")
print(result)