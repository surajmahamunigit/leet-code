# 1.57
import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find minimum eating speed to finish all piles within h hours.

        Args:
            piles: piles[i] bananas in ith pile
            h: given hors to finish all the piles

        Returns:
            minimum eating speed top finish all the piles in h hours

        Time: O(n log m) - m = max(piles), n = len(piles)
        Space: O(1)
        """
        # eating rate would be between 1 and max(piles) -> 1,......, max(piles)
        res = max(piles)
        # use binary search to find minimum rate
        left = 1
        right = max(piles)

        while left <= right:
            mid_rate = (left + right) // 2
            time_to_finish = sum(math.ceil(pile / mid_rate) for pile in piles)
            if time_to_finish <= h:
                res = min(res, mid_rate)
                right = mid_rate - 1
            else:
                left = mid_rate + 1

        return res

s = Solution()
assert s.minEatingSpeed([3,6,7,11], 8) == 4
assert s.minEatingSpeed([30,11,23,4,20], 5) == 30
assert s.minEatingSpeed([5], 5) == 1
assert s.minEatingSpeed([5], 1) == 5
assert s.minEatingSpeed([1000000000], 2) == 500000000
print("passed")

# 2.09 -> 12 min to solve