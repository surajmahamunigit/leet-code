# algorithm
# given piles array containing bananas in each pile and h hours to finish them all
# range to scan for 1 -> max(piles)
# result = max(piles)
# find mid rate -> count time required to finish all piles -> if time taken is less than given time, reduce rate that increases time
# if time_taken <= h -> candidate result = min(result, current rate) -> right = mid rate - 1
# if time take is greater than given time -> increase eating rate -> mid rate + 1
# in end return result
import math
class Solution:
    def eating_rate(self, piles: list[int], h: int) -> int:
        """Find minimum eating rate to finish all piles in h hours.

        Args:
            h: given hours
            piles: piles[i] number of banans in each pile

        Returns:
            minimum eating rate to finish all bananas

        Time: O(n log (m)) - m = eating rate max(piles), n = len(piles)
        Space: O(1)
        """
        res  = max(piles)

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
#res = s.eating_rate(piles = [1,4,3,2], h = 9)
res = s.eating_rate(piles = [25,10,23,4], h = 4)
print(res)