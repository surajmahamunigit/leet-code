# 11.32
# we are given piles and h hors and we have to find out minimum eating speed
# 1 -> max(piles) eating speed range
# binary search pattern
import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find the minimum eating speed with which koko can finish all piles in h hours.

        Args:
            piles: integer array sowing number of bananas in each pile
            h: given time

        Returns:
            minimum eating speed

        Time: O(n log m) - n = len(piles), m = max(piles)
        Space: O(1)
        """

        # 1 -> max(piles)

        res = max(piles)

        left = 1
        right = max(piles)

        while left <= right:
            sp = (left + right) // 2

            time_needed = sum(math.ceil(pile / sp) for pile in piles )

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

# 11.39 -> 7 min to solve