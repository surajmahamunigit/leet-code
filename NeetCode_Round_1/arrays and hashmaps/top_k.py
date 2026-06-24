class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Args:
            nums: List of integers
            k: Tok k numbers

        Returns:
            list[int]: list of top k frequent numbers

        Time: O(n)
        Space: O(n)
        """

        count = {}
        frequency = [[] for occurrence in range(len(nums) + 1)]  # len(num) + 1 -> index starts at 0 -> 0 occurrence, 1 occurrence, 2 occurrences

        # Count the occurrences of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Add {num: occurrence} to bucket list -> occurrence as index
        for num, occurrence in count.items():
            frequency[occurrence].append(num)

        # Get tok k numbers
        result = []

        for index in range(len(frequency)-1, 0, -1):
            for num in frequency[index]:
                result.append(num)

                if len(result) == k:
                    return result


result = Solution().topKFrequent([1,2,3,4,5,5], 1)
print(result)