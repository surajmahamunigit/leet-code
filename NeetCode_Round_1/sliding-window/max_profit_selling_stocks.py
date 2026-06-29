class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Args:
            prices: Integer array containing prices

        Returns:
            maximum profit
        Time:
        Space
        """
        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):

            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                left = right

            right = right + 1

        return max_profit

result = Solution().maxProfit([10,1,5,6,7,1])
print(result)