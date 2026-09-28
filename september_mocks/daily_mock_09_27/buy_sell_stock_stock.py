# 7.54

class Solution:
    def max_profit(self, prices: list[int]) -> int:
        """Find the maximum profit by buying and selling stock.

        Args:
            prices (list[int]): list of integers representing prices of stock

        Returns:
            int: maximum profit by buying and selling stock

        Time: O(n) - n = len(prices)

        Space: O(1)
        """

        # prices = [10,1,5,6,7,1]
        max_profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] <= prices[left]:
                left = right
                right = left + 1
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
                right += 1
        return max_profit

s = Solution()
print(s.max_profit([2,7,11,15]))
print(s.max_profit(prices = [10,1,5,6,7,1]))
print(s.max_profit([]))