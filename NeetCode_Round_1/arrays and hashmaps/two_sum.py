class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Args:
            nums: Integer Array
            target: Integer target

        Returns:
            list[int]: Indices of two numbers sum target

        Time: O(n)
        Space: O(n)
        """

        previous_map = {}

        for index, num in enumerate(nums):

            complement = target - num

            if complement in previous_map:
                return [previous_map[complement], index]

            previous_map[num] = index

        return []

result = Solution().twoSum(nums=[1, 2, 3, 4], target=5)
print(result)
