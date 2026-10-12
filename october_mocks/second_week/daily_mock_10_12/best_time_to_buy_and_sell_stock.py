# 11

# given -> daily price of the stock
# find -> maximum profit made

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """Find the maximum profit made by buying and selling stock.

        Args:
            prices (list[int]): integer array representing prices of stock for each day

        Returns:
            int: maximum profit made by buying and selling stock

        Time complexity: O(n) - n = len(prices)

        Space complexity: O(1)
        """
        if len(prices) < 2:
            return 0

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):

            if prices[left] < prices[right]:
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)
                right += 1
            else:
                left = right
                right = left + 1

        return max_profit

# 11.06 -> 6 minutes to solve problem
# git commit -> feat: add best time to buy and sell stock solution

s = Solution()
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s.maxProfit([7, 6, 4, 3, 1]) == 0
assert s.maxProfit([1]) == 0
assert s.maxProfit([1, 2]) == 1
assert s.maxProfit([2, 1]) == 0
assert s.maxProfit([3, 3, 3]) == 0
assert s.maxProfit([2, 4, 1]) == 2
assert s.maxProfit([3, 2, 6, 5, 0, 3]) == 4
assert s.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 8
assert s.maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2
assert s.maxProfit([5, 4, 3, 2, 1, 10]) == 9
assert s.maxProfit([0, 0, 0, 5]) == 5
assert s.maxProfit([10, 1, 100]) == 99
assert s.maxProfit(list(range(100000, 0, -1))) == 0
assert s.maxProfit(list(range(1, 100001))) == 99999
assert s.maxProfit([5] * 50000 + [1] + [9] * 50000) == 8