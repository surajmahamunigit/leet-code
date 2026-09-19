# 2.32

class Solution:
    def daily_temperature(self, temperatures: list[int]) -> list[int]:
        """Find the days till warmer temperature for each day in array.

        Args:
            temperatures (list[int]): Array of temperatures.

        Returns:
            list[int]: days till warmer temperature for each day in array

        Time: O(n) - len(temperatures)

        Space: O(n)
        """

        result = [0] * len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                stack_day, _ = stack.pop()
                result[stack_day] = day - stack_day

            stack.append([day, temp])

        return result

s = Solution()
print(s.daily_temperature(temperatures = [30,38,30,36,35,40,28]))
print(s.daily_temperature(temperatures = [22,21,20]))