"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Input: nums = [1, 2, 3, 3]
Output: true
"""


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        # Create a Hashset
        hashset=set()

        # Iterate over each element in the array
        for num in nums:

            # If num in hashset, return True
            if num in hashset:
                return True

            # Add num in the hashset
            hashset.add(num)

        # There was no duplicate return False
        return False



s=Solution()
print("Array conatins ducplicates: ",s.hasDuplicate([1, 2, 3, 3]))