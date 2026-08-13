# 11.57

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Return list where each entry is number of days until warmer temp.

        Args:
            temperatures: list of integers representing daily temperature

        Returns:
            res list where res[i] is days until warmer days for ith day

        Time: O(n) - len(temperatures)
        Space: O(n)
        """

        # [73,74,75,71,69,72,76,73]

        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                stack_day, stack_temp = stack.pop()
                res[stack_day] = index - stack_day

            stack.append([index, temp])

        return res

s = Solution()
assert s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert s.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert s.dailyTemperatures([30,60,90]) == [1,1,0]
assert s.dailyTemperatures([100]) == [0]
assert s.dailyTemperatures([]) == []
print("passed")

# 12.09 -> 12 min to finish