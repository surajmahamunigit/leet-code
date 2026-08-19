# 9.47
# given piles of banana and h hours. asked to find minimum rate to finish all bananas in h hours
# we try from 1 -> max(piles) speed -> binary search
# if eating speed takes less than equal to h hors, its good candidate
import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find minimum eating speed to finish all banans in h hours.

        Args:
            piles: p[i] bananas in ith pile
            h: given time

        Returns:
            minimum speed to finish all bananas

        Time: O(n log m) - n = len(piles), m = max(piles)
        Space: O(1)
        """
        res = max(piles)

        # 1, 2, 3, -> max(piles)
        left = 1
        right = max(piles)

        while left <= right:
            sp = (left + right) // 2
            time_needed = sum(math.ceil(pile / sp) for pile in piles)

            if time_needed <= h:
                res = min(res, sp)
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

# 9.56 -> 10 min to solve