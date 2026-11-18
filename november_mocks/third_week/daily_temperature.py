# 10.59

class Solution:
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        """Find out number of days till warmer temperature for each day in given list.

        Args:
            temperatures: list representing temperature for each day in given list.

        Returns:
            list[int]: list representing number of days till warner temperature for each day in given list.

        Time complexity: O(n) - n = len(temperatures)

        Space complexity: O(n) - n = len(temperatures)
        """


        # temperatures = {10,20,40,20,50}

        stack = []
        result = [-1] * len(temperatures)
        for curr_day, curr_temp in enumerate(temperatures):

            while stack and stack[-1][1] < curr_temp:
                prev_day, _ = stack.pop()

                result[prev_day] = curr_day - prev_day

            stack.append([curr_day, curr_temp])

        return result

s = Solution()

def check(values, expected):
    result = s.daily_temperatures(values)
    assert result == expected

check([10,20,30,40], [1,1,1,-1])
check([10], [-1])
check([30,20,10], [-1,-1,-1])
check([10,30,20], [1,-1,-1])

print("all tests passed!")