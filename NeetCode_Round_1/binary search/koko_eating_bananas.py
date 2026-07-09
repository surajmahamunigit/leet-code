import math


class Solution:
    def minEatingRate(self, piles: list[int], hours: int) -> int:
        """
        Args:
            piles: list containing bananas / pile
            hours: total time give to finish all the piles

        Returns:
            min rate with which koko should eat

        Time: n log m - n = len(piles) -> inner for loop, m = max(piles) -> binary search 1 - max(piles)
        Space: O(1)
        """

        left = 1            # min-rate
        right = max(piles)  # max-rate

        result = right      # for safety

        # Binary search
        while left <= right:

            current_eating_rate = (left + right) // 2

            # find out time needed to finish with this rate
            needed_hours = 0

            for pile in piles:

                needed_hours = needed_hours + math.ceil(pile / current_eating_rate)     # pile = total bananas in pile

            # if needed_hours were smaller than given hours, check min eating rate
            if needed_hours <= hours:
                result = min(result, current_eating_rate)

                # check for even smaller eating rate
                right = current_eating_rate - 1

            # if time taken is too long, means eating rate is low
            else:
                left = current_eating_rate + 1

        return result

result = Solution().minEatingRate(piles = [1,4,3,2], hours = 9)
print(result)
