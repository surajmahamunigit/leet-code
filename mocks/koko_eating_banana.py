# algorithm
# given bananas / pile  array and h hours to finish it.
# minimum speed to start eating banana = 1, max speed = max(piles)
# so the range between 1 to max(piles)
# find mid speed, calculate how long it will take to finish all the piles. -> if time taken > given time -> left = mid speed + 1,
# else its good candidate, save as answer and move right = mid speed - 1
# return minimum speed we found

import math
class Solution:
    def min_eating_speed(self,piles: list[int], h: int) -> int:
        """Find minimum easting speed of koko to finish all piles in given h hours.

        Args:
            piles: integer array representing bananas per pile
            h: given hours to finish all piles

        Returns:
            minimum eating speed for koko to finish all bananas in h hours

        Time: n (log m) - n = len(piles), m = max(piles))
        Space: O(1)
        """

        min_speed = 0
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            time_needed = sum(math.ceil(pile / mid) for pile in piles)

            if time_needed <= h:
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1

        return min_speed

s = Solution()
assert s.min_eating_speed(piles = [1,4,3,2], h = 9) == 2
assert s.min_eating_speed(piles = [25,10,23,4], h = 4) == 25
#assert s.min_eating_speed([], 2) == 0
print("passed")