"""
Args:
    list[int]
Output:
    boolean

Time: O(n)  # might need to check every number in array to find duplicate
Space: O(n) # set to store seen numbers
"""

class Solution:
    def has_duplicates(self, nums: list[int]) -> bool:

        seen_before = set()

        for num in nums:

            if num in seen_before:
                return True

            seen_before.add(num)

        return True


result = Solution().has_duplicates([1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
print(result)