# 6.40

import math
class Solution:
    def min_eating_speed(self, piles: list[int], h: int) -> int:
        """Find the minimum eating rate to finish all piles in h hours.

        Args:
            piles (list[int]): a list of integers representing number of banans per pile
            h (int): given time

        Returns:
            int: minimum eating rate

        Time: O(m log n) - m = len(piles), n = max(piles)

        Space: O(1)
        """
        if len(piles) == 0:
            return 0

        left = 1
        right = max(piles)
        min_speed = max(piles)

        while left <= right:
            curr_speed = (left + right) // 2
            time_needed = sum(math.ceil(pile/curr_speed) for pile in piles)

            if time_needed <= h:
                min_speed = min(min_speed, curr_speed)
                right = curr_speed - 1
            else:
                left = curr_speed + 1

        return min_speed

s = Solution()
print(s.min_eating_speed(piles = [1,4,3,2], h = 9))
print(s.min_eating_speed(piles = [], h = 4))

