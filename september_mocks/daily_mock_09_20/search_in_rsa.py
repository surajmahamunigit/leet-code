# 7.03

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the index of target number in given rsa.

        Args:
            nums (list[int]): list of integers
            target (int): target number

        Returns:
            int: index of target number in nums

        Time: O(log n) - n = len(nums)

        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (left + right) // 2

            if nums[index] == target:
                return index

            # if left side of index is sorted
            if nums[left] <= nums[index]:
                if nums[left] <= target < nums[index]:
                    right = index - 1
                else:
                    left = index + 1
            else:
                if nums[index] < target <= nums[right]:
                    left = index + 1
                else:
                    right = index - 1

        return - 1

s = Solution()
print(s.search(nums = [3,4,5,6,1,2], target = 1))
print(s.search(nums = [3,5,6,0,1,2], target = 4))