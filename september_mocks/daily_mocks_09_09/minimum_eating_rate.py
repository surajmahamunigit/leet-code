# 12.32
import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find the minimum eating speed to finish all the piles in h hours.

        Args:
            piles (list[int]): list representing the number of bananas in each pile
            h (int): given time

        Returns:
            int: minimum eating speed

        Time: O(n log m) - n = len(piles), m = max(piles)
        Space: O(1)
        """
        result = max(piles)

        # eating rate => 1-> max(piles)
        left = 1
        right = max(piles)

        while left <= right:

            sp = (left + right) // 2

            time_needed = sum(math.ceil(pile/sp) for pile in piles)

            if time_needed <= h:
                result = min(result, sp)
                right = sp - 1
            else:
                left = sp + 1

        return result

s = Solution()
assert s.minEatingSpeed([3,6,7,11], 8) == 4
assert s.minEatingSpeed([30,11,23,4,20], 5) == 30
assert s.minEatingSpeed([5], 5) == 1
assert s.minEatingSpeed([5], 1) == 5
assert s.minEatingSpeed([1000000000], 2) == 500000000
assert s.minEatingSpeed([10], 3) == 4
print('passed')

# 12.4311 min