# algorithm
# piles = [3,6,7,11], h = 8. given piles with bananas and time to finish all piles
# max(piles) = 11, gives us max eating speed necessary to each pile in 1 hr.
# so our range of eating speed will lie between 1 and max(piles)
# we do the binary search between 1-> max(piles) that take <= given time h
import math


# example
# piles = [3,6,7,11], h = 8, left = 1, right = 11, max= 0
# while left <= right:
# left = 1, right = 11, mid = 6 banans per hr-> time to finish all piles = 1+1+2+2= 6 < given time, max = 6 -> decrease eating speed -> right = mid index -1
# left = 1, right=5, mid = 3 bananas per hr, total time = 1+2+3+4 = 10 -> greater than given time -> left = mid index + 1= 4
# left = 4, right = 5, mid = 4 bananas per hr, total time = 1+2+2+3=8=given hours -> return max = 4 bananas per hr

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find the minimum eating speed to finish all piles in h hours.

        Args:
            piles: a list of piles with bananas
            h: given time to finish all piles

        Returns:
            minimum eating speed of koko to finish all piles in or less than h hours

        Time: O(n log m) - n = len(piles), m = max(piles)
        Space: O(1)
        """
        min_speed = max(piles)          # start from max speed

        left = 1        # minimum eating speed
        right = max(piles)  # mx eating speed

        # 1, 2, 3, ...................., max(piles)

        while left <= right:

            mid_speed = (left+right)//2
            total_time = sum(math.ceil(pile/mid_speed) for pile in piles)

            if total_time <= h:
                min_speed = min(min_speed, mid_speed)
                right = mid_speed - 1
            else:
                left = mid_speed + 1

        return min_speed

s = Solution()
assert s.minEatingSpeed([3,6,7,11], 8) == 4
assert s.minEatingSpeed(piles = [30,11,23,4,20], h = 5) == 30
print("passed")

