# 12.15
# given array represents daily temperature and asked to find days until warmer day for each day

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Find the day until warmer temperature for each day.

        Args:
            temperatures: temperatures for each day

        Returns:
            days until warmer temperature for each day

        Time: O(n) - n = len(temperatures)
        Space: O(n)
        """
        days = [0] * len(temperatures)
        stack = []
        index = 0
        while index < len(temperatures):

            while stack and stack[-1][1] < temperatures[index]:
                stack_index, _ = stack.pop()
                days[stack_index] = index - stack_index

            stack.append([index, temperatures[index]])
            index += 1

        return days

s = Solution()

assert s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert s.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert s.dailyTemperatures([30,60,90]) == [1,1,0]
assert s.dailyTemperatures([100]) == [0]
assert s.dailyTemperatures([]) == []
print("passed")

# 12.24 -> 9 min to solve