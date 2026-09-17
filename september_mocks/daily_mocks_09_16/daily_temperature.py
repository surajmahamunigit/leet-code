# 7.19

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Find how many days till warm temperatures for each day in array.

        Args:
            temperatures (list[int]): Array of temperatures.

        Returns:
            list[int]: Array of days till warm temperatures for each day in array.

        Time: O()

        Space: O()
        """

        # temperatures = [30,38,30,36,35,40,28]

        result = [0] * len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                stack_day, _ = stack.pop()

                result[stack_day] = day - stack_day

            stack.append([day, temp])

        return result

s = Solution()
res = s.dailyTemperatures(temperatures = [30,38,30,36,35,40,28])
print(res)