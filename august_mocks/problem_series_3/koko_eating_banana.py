# 10.35
# given piles array and h hours to finish it. asked to find out minimum eating rate to finish all piles in h hours.
# eating rate 1 -> max(piles)
# binary search

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find minimum eating rate per hour to finish all piles in h hours.

        Args:
            piles: p[i] number of bananas in pile at ith index
            h: given hours to finish it

        Returns:
            minimum eating speed per hour

        Time: O(n log m) - n = len(piles), m = max(piles)
        Space: O(1)
        """

        left = 1                # minimum speed
        right = max(piles)      # max speed

        res = right

        while left <= right:
            sp = (left + right) // 2
            time_needed =  sum(math.ceil(pile / sp) for pile in piles)

            if time_needed <= h:
                res = sp
                right = sp - 1
            else:
                left = sp + 1

        return res

s = Solution()
assert s.minEatingSpeed([3,6,7,11], 8) == 4
assert s.minEatingSpeed([30,11,23,4,20], 5) == 30
assert s.minEatingSpeed([5], 5) == 1
assert s.minEatingSpeed([5], 1) == 5
assert s.minEatingSpeed([1000000000], 2) == 500000000
print("passed")

# 10.43 -> 8 min to solve