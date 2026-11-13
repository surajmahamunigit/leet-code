# 7
import math
class Solution:
    def eating_rate(self, piles: list[int], h: int) -> int:
        """Find the minimum eating rate to finish all the piles within h hours.

        Args:
            piles: list of integer representing number of bananas per pile
            h: given time to finish all the piles

        Returns:
            int: minimum eating rate to finish all the piles

        Time complexity: O(n log (m)) - n = number of piles, m = max(piles)

        Space complexity: O(1)
        """

        # piles = [2, 4, 6, 1], h = 4
        # eating rate -> 1, 2, 3, 4, 5, 6
        left = 1
        right = max(piles)
        eating_rate = right
        while left <= right:
            mid_rate = (left + right) // 2
            required_time = sum(math.ceil(pile/mid_rate) for pile in piles)

            if required_time <= h:
                eating_rate = mid_rate
                right = mid_rate - 1
            else:
                left = mid_rate + 1
        return eating_rate

s = Solution()

def check(values, h, expected):
    result = s.eating_rate(values, h)
    assert result == expected

check([1,3,5,7], 4, 7)
check([1], 4, 1)
check([1,20], 20, 2)
check([1,20],2, 20)
check([30,11,23,4,20], 6, 23)
print("all tests passed")