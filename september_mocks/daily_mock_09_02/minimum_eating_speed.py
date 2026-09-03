# 12.33am

import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find the minimum eating speed per hour to finish all the piles in h or less hours.

        Args:
            piles list[int]: integer array representing number of banans per pile
            h: given hours

        Returns:
            int: minimum eating speed

        Time: O(n log m) - m = max(piles), n = len(piles)
        Space: O(1)
        """
        # eating speed 1 -> max(piles)

        result = max(piles)
        left = 1
        right = max(piles)

        while left <= right:
            sp = (left + right) // 2
            needed_time = sum(math.ceil(pile/sp) for pile in piles)

            if needed_time <= h:
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
print("passed")


# 12.57 -> 24 min