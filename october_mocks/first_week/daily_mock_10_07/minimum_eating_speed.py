# 11.04
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find the minimum eating speed to finish all piles in h hours.

        Args:
            piles (list[int]): list of integers representing number of bananas per pile
            h (int): given time to finish all piles

        Returns:
            int: minimum eating speed to finish all piles in h hours

        Time complexity: O(n * log m) - n = len(piles), m = max(piles)

        Space complexity: O(1)
        """
        min_eating_speed = max(piles)
        left = 1
        right = max(piles)

        while left <= right:
            speed = (left + right) // 2

            time_needed = sum(math.ceil(pile / speed) for pile in piles)

            if time_needed <= h:
                min_eating_speed = speed
                right = speed - 1
            else:
                left = speed + 1

        return min_eating_speed

# 11.12 -> 8 minutes to solve the problem
# git commit -> feat: add koko eating banana solution

s = Solution()
assert s.minEatingSpeed([3,6,7,11], 8) == 4
assert s.minEatingSpeed([30,11,23,4,20], 5) == 30
assert s.minEatingSpeed([30,11,23,4,20], 6) == 23
assert s.minEatingSpeed([5], 5) == 1
assert s.minEatingSpeed([5], 1) == 5
assert s.minEatingSpeed([10], 3) == 4
assert s.minEatingSpeed([1000000000], 2) == 500000000
assert s.minEatingSpeed([1,1,1,10], 4) == 10