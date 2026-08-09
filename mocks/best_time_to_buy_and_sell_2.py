# algorithm
# given integer array representing daily stock prices and we have to find out max profit we can make by buying stock one day and selling it nother.
# assume two pointers left=0 and right and max_profit = 0
# while left < right -> right = left + 1
# if prices[right] <= prices[left] -> left = right, right = right + 1
# else curr_profit = prices[right] - prices[left], compare max_profit with urr_profit and save max profit
# end return max_profit

class Solution:
    def max_profit(self, prices: list[int]) -> int:
        """Find maximum profit by buying and selling stocks.

         Args:
             prices: list of integers representing the daily stock prices.

         Returns:
             maximum profit

         Time: O(n) - n = len(prices)
         Space: O(1)
         """
        max_profit = 0
        left = 0
        right = left + 1

        while right < len(prices):

            if prices[right] <= prices[left]:
                left = right
                right = left + 1
            else:
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)
                right += 1

        return max_profit

s = Solution()
#res = s.max_profit(prices = [10,1,5,6,7,1])
res = s.max_profit(prices = [10,8,7,5,2])
print(res)