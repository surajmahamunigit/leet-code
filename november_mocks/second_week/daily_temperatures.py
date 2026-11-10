# 3.08

class Solution:
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        """Find the days till warmer temperature for each day in given list.

        Args:
            temperatures: list representing temperatures for i'th day

        Returns:
            list[int]: list representing days till warmer temperature for i'th day

        Time complexity: O(n) - len(temperatures)

        Space complexity: O(n)
        """

        result = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                previous_day, _ = stack.pop()
                result[previous_day] = day - previous_day

            stack.append((day, temp))
        return result

s = Solution()

def check(values, expected):
    result = s.daily_temperatures(values)
    assert result == expected

check([10, 20, 30], [1,1,0])
check([30,20,10], [0,0,0])
check([10,20,5], [1,0,0])
check([10,10,10],[0,0,0])
print("all tests passed")

# 3.20 -> 12 minutes to solve
# git commit -> feat: add daily temperatures solution