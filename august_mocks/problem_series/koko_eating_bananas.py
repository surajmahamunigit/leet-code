# 4.15
# given integer array showing number of bananas per pile and h hours to finish it.
# asked to find how many bananas per hour koko should it. keep it lowest
# binary search patter -> search range 1 -> max(piles)
# if you finish faster -> you are eating too fast -> reduce speed

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find lowest eating rate to finish all pile sin h hours.

        Args:
            piles: piles[i] is number of bananas per pile
            h: given hours

        Returns:
            minimum banana eating rate possible

        Time: O(n log m) - n = len(piles), m = max(piles)
        Space: O(1)
        """
        res = max(piles) # please start at max speed and return the lowest speed

        # eating rate
        left = 1
        right = max(piles)

        while left <= right:
            mid_sp = (left + right) // 2
            time_needed = sum(math.ceil(pile/mid_sp) for pile in piles)

            if time_needed <= h:
                res = min(mid_sp, res)
                right = mid_sp - 1
            else:
                left = mid_sp + 1

        return res

s = Solution()
res = s.minEatingSpeed(piles=[312884470], h=312884469)
print(res)
# 4.48 -> 33 min to solve
# add to next 3 days surface list