# 9.21

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Find the days till warmer day for each day in the given temperatures arra.

        Args:
            temperatures (list[int]): list of daily temperatures

        Returns:
            list[int]: list of days till warmer day

        Time: O(n) - n = len(temperatures)
        Space: O(n)
        """
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                stack_index, _ = stack.pop()
                result[stack_index] = index - stack_index

            stack.append([index, temp])

        return result

s = Solution()
assert s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert s.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert s.dailyTemperatures([30,60,90]) == [1,1,0]
assert s.dailyTemperatures([100]) == [0]
assert s.dailyTemperatures([]) == []
print("passed")

# 9.28 -> 7 min to solve