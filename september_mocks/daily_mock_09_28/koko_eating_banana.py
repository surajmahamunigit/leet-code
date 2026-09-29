# 8.45

import math
class Solution:
    def min_eating_rate(self, piles: list[int], h : int) -> int:
        """Find the minimum eating rate to finish all the piles in h hours.

        Args:
            piles (list[int]): list of integers representing the piles of bananas.
            h (int): given time

        Returns:
            int: minimum eating speed

        Time complexity: O(m * log n) - n = max(piles), m = len(piles)

        Space complexity: O(1)
        """

        # Input: piles = [1,4,3,2], h = 9

        # eating rate -> 1 -> max(piles)
        min_rate = max(piles)
        left = 1
        right = max(piles)
        while left <= right:
            curr_speed = (left + right) // 2
            time_needed = sum(math.ceil(pile/curr_speed) for pile in piles)

            if time_needed <= h:
                min_rate = min(min_rate, curr_speed)
                right = curr_speed - 1
            else:
                left = curr_speed + 1

        return min_rate

s = Solution()
print(s.min_eating_rate(piles=[2,3,4,5], h=5))
print(s.min_eating_rate(piles=[1, 4, 3, 2], h=9))
print(s.min_eating_rate([1,1,1,10], h = 4))