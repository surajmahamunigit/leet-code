# 12.24
# given -> piles of banans and h hours to finish all.
# asked ->  find minimum eating rate to finish ll bananas
import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find minimum eating rate to finish all piles in h hours.

        Args:
            piles (list[int]): list of integers representing number of bananas in each pile
            h (int): given time to finish all piles

        Returns:
            int: minimum eating rate to finish all piles in h hours

        Time complexity: O(n log(m)) - m = max(piles), n = len(piles)

        Space complexity: O(1)
        """

        # eating speed -> 1 -> max(piles)
        left = 1
        right = max(piles)

        min_speed = max(piles)

        while left <= right:
            curr_speed = (left + right) // 2
            needed_time = sum(math.ceil(pile/curr_speed) for pile in piles)

            if needed_time <= h:
                min_speed = min(min_speed, curr_speed)
                right = curr_speed - 1
            else:
                left = curr_speed + 1

        return min_speed

# 12.35 -> 11 minutes to solve problem
# git commit -> feat: add koko eating bananas solution

s = Solution()
assert s.minEatingSpeed([30,11,23,4,20], 6) == 23
assert s.minEatingSpeed([312884470], 312884469) == 2
assert s.minEatingSpeed([1,1,1,1], 4) == 1
assert s.minEatingSpeed([2,2], 3) == 2
assert s.minEatingSpeed([10,1,1], 5) == 4
assert s.minEatingSpeed([7,7,7], 6) == 4
assert s.minEatingSpeed([9,9,9,9,9], 10) == 5
assert s.minEatingSpeed([1,2,3,4,5,6,7,8,9,10], 55) == 1
assert s.minEatingSpeed([10**9, 10**9], 3) == 10**9
assert s.minEatingSpeed([10**9] * 10**4, 10**4) == 10**9
assert s.minEatingSpeed([10**9] * 10**4, 2 * 10**4) == 5 * 10**8