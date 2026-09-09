# 7.40

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Find out days till warmer day for each day in given temperatures list.

        Args:
            temperatures (list[int]): list of integers representing daily temperatures

        Returns:
            list(int): list representing days till warmer day for each day in given temperatures list.

        Time: O(n) - n = len(temperatures)
        Space: O(n)
        """

        result = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                stack_day, stack_temp = stack.pop()
                result[stack_day] = day - stack_day

            stack.append([day, temp])

        return result

s = Solution()
assert s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert s.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert s.dailyTemperatures([30,60,90]) == [1,1,0]
assert s.dailyTemperatures([100]) == [0]
assert s.dailyTemperatures([]) == []
print('passed')

# 7.50 -> 10 min solve