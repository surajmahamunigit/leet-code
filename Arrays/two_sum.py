"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input:
nums = [3,4,5,6], target = 7

Output: [0,1]

Time complexity: O(n) -> to traverse the array
Space complexity: O(n) -> for map
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        prevmap={}

        for index, num in enumerate(nums):
            diff=target-num

            # Check if diff is in map or not
            if diff in prevmap:
                return [prevmap[diff],index]

            # If not present,
            prevmap[num]=index


s=Solution()
result=s.twoSum([3,4,5,6],7)

print(result)