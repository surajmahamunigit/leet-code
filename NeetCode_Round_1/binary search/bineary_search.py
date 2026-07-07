class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Args:
            nums: list of integers
            target: num to find within nums

        Returns:
            index of target num if present, otherwise -1

        Time:
        Space:
        """
        left = 0
        right = len(nums) - 1

        while left <= right:

            # find mid index
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                return mid      # return index, not value

        return -1

result = Solution().search(nums=[1, 3, 5, 6, 7, 8, 9], target=9)
print(result)