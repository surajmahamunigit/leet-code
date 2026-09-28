# 3.14

class Solution:
    def daily_temperature(self, temperatures: list[int]) -> list[int]:
        """Find the number of days till warm day for each day in array.

        Args:
            temperatures (list[int]): list of integers representing daily temperatures

        Returns:
            list[int]: list of integers representing number of days till warmer temperatures

        Time: O(n) - n = len(temperatures)

        Space: O(n)
        """

        # temperatures = [30,38,30,36,35,40,28]

        result = [0] * len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                stack_day, stack_temp = stack.pop()
                result[stack_day] = day - stack_day

            stack.append([day, temp])
        return result

s = Solution()
print(s.daily_temperature(temperatures = [30,38,30,36,35,40,28]))
print(s.daily_temperature([20, 21, 22]))
print(s.daily_temperature([22, 21, 20]))