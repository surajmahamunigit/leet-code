class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Args:
            temperatures: list of integers representing daily temperature

        Returns:
            list[int]: list of number of days before warmer temperature

        Time: O(n) - n = len(temperatures)
        Space: O(n) - for stack
        """

        result = [0] * len(temperatures)    # for each day
        stack = []  # stores [temp, index]

        for current_day, current_temp in enumerate(temperatures):

            # if stack is not empty, and current_temp > stack_temp (for older days)
            while stack and current_temp > stack[-1][0]:
                _, stack_day = stack.pop()

                result[stack_day] = current_day - stack_day

            stack.append([current_temp, current_day])       # append as list [temp: day] together

        return result

result = Solution().dailyTemperatures([30,38,30,36,35,40,28])
print(result)