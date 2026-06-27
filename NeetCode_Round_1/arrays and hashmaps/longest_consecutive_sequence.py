class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Args:
            nums: list of integers

        Returns:
            length of longest consecutive sequence

        Time: O(n) - for all the elements in array
        Space: O(n) - to store nums set
        """

        # Convert the nums array to set for O(1) lookup
        nums_set = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in nums_set:
                length = 0
                while (num+length) in nums_set:
                    length += 1

                longest = max(longest, length)

        return longest

result = Solution().longestConsecutive([1,2,3,5,7,0])
print(result)