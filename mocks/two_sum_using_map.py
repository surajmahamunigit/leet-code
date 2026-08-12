# algorithm
# given nums = [1,2,3,4,5] not sorted array, and target
# asked to return indices of [smaller numer, bigger number]
# for each number in nums ->
# compliment = target - number ,
# check if compliment exist in seen map if it does -> return its index, current numbers index
# else store current number : its index as key:value in seen map

class Soluton:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """Find and return indices of two numbers that add up to target.

        Args:
            nums: list of integers
            target: target number

        Returns:
            list of indices pf two numbers that add up to target, else []

        Time: O(n) - n = len(nums)
        Space: O(n)
        """
        seen = {}

        for index, num in enumerate(nums):

            compliment = target - num
            # check if comp is there -> if yes, seen[comp] will give us its index.
            if compliment in seen:
                return [seen[compliment], index]

            seen[num] = index

        return []

