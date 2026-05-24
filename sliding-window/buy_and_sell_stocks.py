"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6

Time: O(n)
Space: O(1)
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        left_index = 0
        right_index = 1
        max_profit = 0

        while right_index < len(prices):

            # Profitable :
            if prices[left_index] < prices[right_index]:
                profit = prices[right_index] - prices[left_index]
                max_profit = max(max_profit, profit)

            else:
                left_index = right_index

            right_index += 1

        return max_profit


result = Solution().maxProfit([10,1,5,6,7,1])
print(result)
