# 2.13

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Find the number of days until warmer temperature foreach day in temperatures array.

        Args:
            temperatures (list[int]): list representing the daily temperatures

        Returns:
            list[int]: list representing the number of days until warmer temperature

        Time: O(n) - n = len(temperatures)
        Space: O(n)
        """
        result = [0] * len(temperatures)
        stack = []

        for day in range(len(temperatures)):

            while stack and stack[-1][1] < temperatures[day]:
                stack_day, _ = stack.pop()
                result[stack_day] = day - stack_day

            stack.append([day, temperatures[day]])

        return result

s = Solution()
assert s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert s.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert s.dailyTemperatures([30,60,90]) == [1,1,0]
assert s.dailyTemperatures([100]) == [0]
assert s.dailyTemperatures([]) == []
print("passed")

# 2.24 -> 11 min