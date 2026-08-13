# 7.27

class Solution:
    def max_profit(self, prices: list[int]) -> int:
        """Find max profit by buying and selling stock.

        Args:
            prices: prices[i] price of stock on day i

        Returns:
            max profit generated

        Time: O(n) - n = len(prices)
        Space: O(1)
        """

        # [7,1,5,3,6,4]
        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):

            if prices[left] >= prices[right]:
                left = right
            else:
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)

            right += 1

        return max_profit

s = Solution()
assert s.max_profit([7,1,5,3,6,4]) == 5      # classic case
assert s.max_profit([7,6,4,3,1]) == 0        # strictly decreasing
assert s.max_profit([]) == 0                 # empty
assert s.max_profit([5]) == 0                # single day
assert s.max_profit([1,2,3,4,5]) == 4        # strictly increasing
print("passed")

# 7.37 -> 10 min