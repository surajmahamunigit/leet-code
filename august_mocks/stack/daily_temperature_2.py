# 2.22

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Find out days to warmer temperature for each day in given array.

        Args:
            temperatures: array representing every day temperature

        Returns:
            array containing days till warmer temperature for each day in given array

        Time: O(n) - n = len(temp)
        Space: O(n)
        """
        res = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                stack_day, stack_temp = stack.pop()
                res[stack_day] = day - stack_day

            stack.append([day, temp])

        return res

s = Solution()
assert s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert s.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert s.dailyTemperatures([30,60,90]) == [1,1,0]
assert s.dailyTemperatures([100]) == [0]
assert s.dailyTemperatures([]) == []
print("passed")

# 2.29 -> 7 min to solve