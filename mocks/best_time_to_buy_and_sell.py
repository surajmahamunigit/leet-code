# algorithm
# use two pointers left = 0 and right = 1
# while right < len(prices):
# if price[right] <= price[left] -> left = right, right = left + 1
# if not, then find curr_profit = prices[right] - prices[left], compare with max_profit = max(max_profit, curr_profit), move right forward by 1
# in end return max_profit
# 8 min

# example
# prices = [10,1,5,6,7,1], left = 0, right = 1, max_profit = 0
# left = 0, right = 1 -> 1 < 10, left = right = 1, right = 2
# left 1, right = 2 -> 1< 5 -> curr_profit = 5-1 = 4, max_profit = 4, right = 3
# left 1, right =3 -> 1< 6 -> curr_profit = 6-1 = 5, max_profit = 5, right = 4
# left 1, right =4 -> 1< 7 -> curr_profit = 7-1 = 6, max_profit = 6, right = 5
# left 1, right =5 -> 1<= 1 ->left=5, right = 6
# return max_profit = 6
# 6 min

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """Find the maximum profit by buying and selling stocks on different days.

        Args:
            prices: integer array representing daily stock prices

        Returns:
            maximum profit generated

        Time: O(n) - n = len(prices)
        Space: O(1)
        """

        max_profit = 0

        left = 0
        right = 1

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
assert s.maxProfit(prices = [10,1,5,6,7,1]) == 6
assert s.maxProfit(prices = [10,8,7,5,2]) == 0
print("passed")

# 8 min