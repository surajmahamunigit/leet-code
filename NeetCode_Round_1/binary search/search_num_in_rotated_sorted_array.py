class Solution:
    def searchNum(self, nums: list[int], target: int) -> int:
        """
        Args:
            nums: list of integers
            target: number to search within nums

        Returns:
            target num index if found, otherwise -1

        Time: O(log n) - n = len(nums)
        Space: O(1)

        """

        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2
            middle_num = nums[middle]


            # [3,  4,  5,  6,   1,  2 ]
            #  |left-sort  |    |R.S|

            # case 1
            if target == middle_num:
                return middle

            # we are trying to figure out which side of middle_num is sorted
            # case 2: left side sorted or not
            if nums[left] <= middle_num:

                if target > middle_num or target < nums[left]:
                    left = middle + 1

                else:
                    right = middle - 1


            # case 3: right side sorted or not
            else:

                if target < middle_num or target > nums[right]:
                    right = middle - 1

                else:
                    left = middle + 1

        return -1

result = Solution().searchNum([1,2,3,4,5,6,7,8,9], 0)
print(result)