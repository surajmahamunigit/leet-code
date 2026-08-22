# 3.28
# given prices array that represents prices of stock on different days and asked to find most profit made
# two pointer pattern
# one pointer at left = 0 and second at right = left  + 1
# if price[left] >= price[right] -> left = right, right = left + 1
# else calculate profit and keep track of it

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """Find the maximum profit made by buying and selling stock on different days.

        Args:
            prices: integer array representing prices of stock at different days

        Returns:
            maximum profit made by buying and selling stock on different days

        Time: O(n) - n  = len(prices)
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
assert s.maxProfit([7,1,5,3,6,4]) == 5
assert s.maxProfit([7,6,4,3,1]) == 0
assert s.maxProfit([]) == 0
assert s.maxProfit([5]) == 0
assert s.maxProfit([1,2,3,4,5]) == 4
print("passed")


# 3.38 -> 10 min to solve