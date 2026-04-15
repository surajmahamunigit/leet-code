"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Input: nums = [1, 2, 3, 3]
Output: true
"""

"""Time complexity is O(n) and space complexity is O(n) due to the set"""


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        # Iterate over each element in the array

        seen=set()

        for num in nums:

            # If num in seen, return True
            if num in seen:
                return True


            seen.add(num)

        # There was no duplicate return False
        return False



s=Solution()
print("Array conatins ducplicates: ",s.hasDuplicate([1, 2, 3, 3]))



################ Method 2 ################

# If extra space is not allowed, I can sort the array and check adjacent elements in O(n log n) time.