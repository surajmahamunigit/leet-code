# algorithm
# given temp =  [30,38,30,36,35,40,28]
# we will use stack to solve this problem. hint in this problem is we if we cant just add temp to stack, we will need to add its index with it
# so we can process it when we find warmer temp day
# so stack = []
# start from first index -> if stack is empty , add [index, temp] to the stack
# if its not empty -> compare stack[-1][1] < current temp -> pop the stack, count current index - stack_index and add to result array at same index
# if its not small then just add  to the stack as [current_index, temp]
# in end return result


class Solution:
    def daily_temperature(self, temp: list[int]) -> list[int]:
        """For each day, return number of days until warmer temperature.

        Args:
            temp: list of integers representing daily temp.

        Returns:
            list where result[i] = days until warmer day, else 0

        Time: O(n) - n = len(temp)
        Space: O(n)
        """

        result = [0] * len(temp)
        stack = []

        # temperatures = [30,38,30,36,35,40,28]
        for index in range(len(temp)):
            curr_temp = temp[index]
            while stack and curr_temp > stack[-1][1]:
                stack_index, _ = stack.pop()
                result[stack_index] = index - stack_index

            stack.append([index, curr_temp])

        return result

s = Solution()
#res = s.daily_temperature(temp = [30,38,30,36,35,40,28])
res = s.daily_temperature(temp = [22,21,20])
print(res)